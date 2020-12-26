#include <cstdio>
#include <string>
#include <set>

struct Node
{
    int val;
    Node *lc;
    Node *rc;

    Node() : val(0), lc(NULL), rc(NULL)
    {
    }
};

using namespace std;

void insert(Node *root, Node *node)
{
    if (node->val < root->val)
    {
        if (root->lc)
        {
            insert(root->lc, node);
        }
        else
        {
            root->lc = node;
        }
    }
    else
    {
        if (root->rc)
        {
            insert(root->rc, node);
        }
        else
        {
            root->rc = node;
        }
    }
}

void stringify(Node *root, string &name)
{
    if (root->lc)
    {
        name.append("L");
        stringify(root->lc, name);
    }
    if (root->rc)
    {
        name.append("R");
        stringify(root->rc, name);
    }
    name.append("U");
}

int main()
{
    int nTrees, nLayers;
    scanf("%d %d", &nTrees, &nLayers);
    set<string> names;
    for (int ii = 0; ii < nTrees; ++ii)
    {
        Node *root = new Node;
        scanf("%d", &root->val);
        for (int jj = 1; jj < nLayers; ++jj)
        {
            Node *node = new Node;
            scanf("%d", &node->val);
            insert(root, node);
        }

        string name("");
        stringify(root, name);
        names.insert(name);
        //fprintf(stderr, "%s\n", name.c_str());
    }
    printf("%d\n", (int)names.size());
    return 0;
}