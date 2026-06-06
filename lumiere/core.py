"""
Core business logic for Lumière pricing engine.
"""

class PricingEngine:
    """Handles all pricing calculations and profit margin management."""
    
    # Default category margins (can be customized)
    DEFAULT_MARGINS = {
        "Gems & Stones": 0.70,      # 70% target margin
        "Silver Chains": 0.55,       # 55% target margin
        "Rings": 0.65,               # 65% target margin
        "Custom Orders": 0.75        # 75% target margin
    }
    
    HEALTHY_MARGIN_THRESHOLD = 35  # 35% profit margin benchmark
    
    def __init__(self, startup_capital=45000, revenue_target=380000, profit_target=148000):
        """
        Initialize the pricing engine with business parameters.
        
        Args:
            startup_capital: Initial investment amount
            revenue_target: Annual revenue target
            profit_target: Annual profit target
        """
        self.startup_capital = startup_capital
        self.revenue_target = revenue_target
        self.profit_target = profit_target
        self.category_margins = self.DEFAULT_MARGINS.copy()
        
    def calculate_business_health(self):
        """
        Calculate overall business profit margin health.
        
        Returns:
            dict: Contains profit_margin_percentage and health_status
        """
        if self.revenue_target == 0:
            return {"profit_margin_percentage": 0, "health_status": "ERROR"}
        
        profit_margin = (self.profit_target / self.revenue_target) * 100
        
        if profit_margin >= self.HEALTHY_MARGIN_THRESHOLD:
            health_status = "HEALTHY (High Margin Venture)"
        else:
            health_status = "WARNING (Review Pricing Strategy)"
        
        return {
            "profit_margin_percentage": round(profit_margin, 2),
            "health_status": health_status
        }
    
    def get_category_margin(self, category):
        """
        Get the target margin for a product category.
        
        Args:
            category: Product category name
            
        Returns:
            float: Margin as decimal (0.70 = 70%)
            
        Raises:
            ValueError: If category not found
        """
        if category not in self.category_margins:
            raise ValueError(f"Category '{category}' not found. Available: {list(self.category_margins.keys())}")
        return self.category_margins[category]
    
    def set_category_margin(self, category, margin):
        """
        Update the target margin for a category.
        
        Args:
            category: Product category name
            margin: Margin as decimal (0.70 for 70%)
        """
        if not 0 <= margin < 1:
            raise ValueError("Margin must be between 0 and 1 (0-100%)")
        self.category_margins[category] = margin
    
    def get_all_categories(self):
        """Return list of available product categories."""
        return list(self.category_margins.keys())
