const { execSync } = require('child_process');

function generateHtml(projectId, token) {
    // Construct the Python command with arguments
    const pythonCommand = `python3 -m notion_graph ${projectId} ${token}`;

    try {
        // Execute the Python script and get the output
        const output = execSync(pythonCommand).toString();

        return output;
    } catch (error) {
        console.error('Error executing Python script:', error);
        return null;
    }
}

module.exports.generateHtml = generateHtml;