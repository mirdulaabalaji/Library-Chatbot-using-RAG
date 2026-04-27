def node_to_text(node):
    props = dict(node)
    label = list(node.labels)[0]
    
    if label == "Book":
        return f"{props.get('title')}: {props.get('description')}"
    elif label == "Author":
        return f"Author: {props.get('name')}"
    elif label == "Genre":
        return f"Genre: {props.get('name')}"
    elif label == "Trope":
        return f"Trope: {props.get('name')}"
    elif label == "Publisher":
        return f"Publisher: {props.get('name')}"
    elif label == "LibraryBranch":
        return f"Library Branch: {props.get('name')}"
    elif label == "Member":
        return f"Member: {props.get('name')} (ID: {props.get('mid')})"
    else:
        return str(props)