import math

class IncrementalSearch:
    @staticmethod
    def incremental_search(f, xinit, dx, n, tolerance=1e-6):
        results = []
        x0 = float(xinit)
        dx = float(dx)
        tolerance = float(tolerance)
        iteration = 1

        # Definir un entorno seguro para eval
        safe_dict = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        safe_dict['x'] = x0

        try:
            fx0 = eval(f, {"__builtins__": None}, safe_dict)
        except Exception as e:
            return None, f"Error evaluating function: {str(e)}"

        if abs(fx0) < tolerance:
            return results, f"An approximation of the root was found for x = {x0}"

        for i in range(1, n + 1):
            x1 = x0 + dx
            safe_dict['x'] = x1
            try:
                fx1 = eval(f, {"__builtins__": None}, safe_dict)
            except Exception as e:
                return results, f"Error evaluating function: {str(e)}"

            if abs(fx1) < tolerance:
                results.append(f"There's a root for the function in [{x0}, {x1}]")
            elif fx0 * fx1 < 0:
                results.append(f"There's a root for the function in [{x0}, {x1}]")

            x0 = x1
            fx0 = fx1

        return results, "Incremental search completed."
