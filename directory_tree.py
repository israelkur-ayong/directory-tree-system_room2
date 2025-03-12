class DirectoryNode:
    """Represents a directory in the tree."""
    def __init__(self, name):
        self.name = name
        self.children = {}

    def add_child(self, child_name):
        """Adds a new directory under this node."""
        if child_name not in self.children:
            self.children[child_name] = DirectoryNode(child_name)

    def remove_child(self, child_name):
        """Removes a directory and its subdirectories."""
        if child_name in self.children:
            del self.children[child_name]

class DirectoryTree:
    """Manages the directory tree structure."""
    def __init__(self, root_name="Root"):
        self.root = DirectoryNode(root_name)

    def find_directory(self, node, name):
        """Finds a directory node by name."""
        if node.name == name:
            return node
        for child in node.children.values():
            found = self.find_directory(child, name)
            if found:
                return found
        return None

    def add_directory(self, parent_name, child_name):
        """Adds a directory at any level."""
        parent_node = self.find_directory(self.root, parent_name)
        if parent_node:
            parent_node.add_child(child_name)
        else:
            print(f"Error: Parent '{parent_name}' not found.")

    def delete_directory(self, parent_name, child_name):
        """Deletes an existing directory and its subdirectories."""
        parent_node = self.find_directory(self.root, parent_name)
        if parent_node and child_name in parent_node.children:
            parent_node.remove_child(child_name)
        else:
            print(f"Error: Directory '{child_name}' not found under '{parent_name}'.")

    def print_tree(self, node=None, level=0):
        """Prints the directory structure."""
        if node is None:
            node = self.root
        print(" " * (level * 4) + f"└── {node.name}")
        for child in node.children.values():
            self.print_tree(child, level + 1)

# Example Usage
if __name__ == "__main__":
    tree = DirectoryTree("Pictures")
    tree.add_directory("Pictures", "Saved Pictures")
    tree.add_directory("Saved Pictures", "Web Images")
    tree.add_directory("Web Images", "Chrome")
    tree.add_directory("Web Images", "Opera")
    tree.add_directory("Web Images", "Firefox")
    tree.add_directory("Pictures", "Screenshots")
    tree.add_directory("Pictures", "Camera Roll")
    tree.add_directory("Camera Roll", "2025")
    tree.add_directory("Camera Roll", "2024")
    tree.add_directory("Camera Roll", "2023")

    print("\nInitial Directory Structure:")
    tree.print_tree()

    tree.delete_directory("Saved Pictures", "Web Images")
    print("\nAfter Deleting 'Web Images':")
    tree.print_tree()

