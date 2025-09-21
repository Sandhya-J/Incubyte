import { useState } from 'react'
import './App.css'

function App() {
  const [numbers, setNumbers] = useState('')
  const [result, setResult] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const calculate = async () => {
    if (!numbers.trim()) {
      setError('Please enter some numbers')
      return
    }

    setLoading(true)
    setError('')
    setResult('')

    try {
      const processedNumbers = numbers.replace(/\\n/g, '\n')
      
      const response = await fetch('/api/calculate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ numbers: processedNumbers }),
      })

      const data = await response.json()

      if (response.ok) {
        setResult(data.result)
      } else {
        setError(data.detail || 'An error occurred')
      }
    } catch (err) {
      setError('Failed to connect to the server. Make sure the backend is running.')
    } finally {
      setLoading(false)
    }
  }

  const clearAll = () => {
    setNumbers('')
    setResult('')
    setError('')
  }

  return (
    <div className="app">
      <div className="calculator">
        <h1>String Calculator</h1>
        
        <div className="input-section">
          <label htmlFor="numbers">Enter numbers (comma-separated or with newlines):</label>
          <textarea
            id="numbers"
            value={numbers}
            onChange={(e) => setNumbers(e.target.value)}
            placeholder="Example: 1,2,3 or 1\n2,3 or //;\n1;2;3"
            rows={4}
          />
        </div>

        <div className="button-section">
          <button onClick={calculate} disabled={loading}>
            {loading ? 'Calculating...' : 'Calculate'}
          </button>
          <button onClick={clearAll} className="clear-btn">
            Clear
          </button>
        </div>

        {result !== '' && (
          <div className="result-section">
            <h3>Result:</h3>
            <div className="result">{result}</div>
          </div>
        )}

        {error && (
          <div className="error-section">
            <h3>Error:</h3>
            <div className="error">{error}</div>
          </div>
        )}

        <div className="examples">
          <h3>Examples:</h3>
          <ul>
            <li><code>1,2,3</code> → 6</li>
            <li><code>1\n2,3</code> → 6 (use actual newline or type \n)</li>
            <li><code>//;\n1;2;3</code> → 6</li>
            <li><code>1,2\n3,4</code> → 10</li>
          </ul>
        </div>
      </div>
    </div>
  )
}

export default App
