from flask import Flask, request, jsonify
from app import app

@app.route('/recommendation', methods=['POST'])
def recommend():
    data = request.get_json()
    functionality = data.get('functionality')
    performance_requirements = data.get('performance_requirements')
    codebase_size_estimation = data.get('codebase_size_estimation')

    # Call the SustainableDev AI function to get the recommendation
    sustainable_dev_ai_response = app.run(debug=False, threaded=True, port=5001)
    sustainable_dev_ai_response.post({
        'functionality': functionality,
        'performance_requirements': performance_requirements,
        'codebase_size_estimation': codebase_size_estimation
    })

    # Get the recommendation from the SustainableDev AI
    recommendation = sustainable_dev_ai_response.get_json()['language']
    energy_savings = sustainable_dev_ai_response.get_json()['energy_savings']

    return jsonify({
        'recommendation': recommendation,
        'energy_savings': energy_savings
    })

if __name__ == '__main__':
    app.run(debug=True)
