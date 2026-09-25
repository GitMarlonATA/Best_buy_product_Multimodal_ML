import os
import sys

os.environ.setdefault("TF_USE_LEGACY_KERAS", "1")

import tf_keras
sys.modules["tensorflow.keras"] = tf_keras
for sub in ["layers", "models", "applications", "preprocessing",
            "preprocessing.image", "utils", "optimizers", "losses", "callbacks"]:
    try:
        sys.modules[f"tensorflow.keras.{sub}"] = __import__(
            f"tf_keras.{sub}", fromlist=["_"]
        )
    except ImportError:
        pass
