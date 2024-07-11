Sure, let's expand your `README.md` to include instructions for installing Node.js 10, the semistandard linter, and the request module. Additionally, I'll show how to set the `NODE_PATH`.

Here's how your `README.md` might look:

```markdown
# Star Wars Characters Script

This script fetches and prints all characters of a specified Star Wars movie using the Star Wars API.

## Usage

```bash
./starwars_characters.js <movie_id>
```

Replace `<movie_id>` with the ID of the Star Wars movie.

## Requirements

- Ubuntu 20.04 LTS
- Node.js (version 10.14.x)
- semistandard
- request

## Installation

### Install Node.js 10

```bash
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Install semistandard

```bash
sudo npm install semistandard --global
```

### Install request module

```bash
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
```

## Example

```bash
./starwars_characters.js 3
```

## Running the Script

1. Ensure the script is executable:

```bash
chmod +x starwars_characters.js
```

2. Run the script with the desired movie ID:

```bash
./starwars_characters.js <movie_id>
```
