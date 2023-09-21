
document.addEventListener('DOMContentLoaded', (event) => {
    const deployButton = document.getElementById('deploy-button');
    const agentNameInput = document.getElementById('agent-name-input');
    const sampleQuestionsInput = document.getElementById('sample-questions-input');
    const apiKeyInput = document.getElementById('api-key-input');

    deployButton.addEventListener('click', () => {
        const agentName = agentNameInput.value;
        const sampleQuestions = sampleQuestionsInput.value;
        const apiKey = apiKeyInput.value;

        fetch('/api/ai_agent/deploy', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                agent_name: agentName,
                sample_questions: sampleQuestions,
                api_key: apiKey,
            }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('AI agent deployed successfully!');
            } else {
                alert('Failed to deploy AI agent. Please try again.');
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});
