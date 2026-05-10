from . import base_types
import InvestmentPlan16
import DataModification1Code

class ModificationScope41(base_types._BaseFieldType):

	__slots__ = ["_InvstmtPlan", "_ModScpIndctn"]
	@property
	def InvstmtPlan(self):
		return self._InvstmtPlan

	@InvstmtPlan.setter
	def InvstmtPlan(self, value):
		self._InvstmtPlan = value if type(value) != auto else self.make_default("InvstmtPlan")

	@InvstmtPlan.deleter
	def InvstmtPlan(self):
		del self._InvstmtPlan
		self._InvstmtPlan = None

	@property
	def ModScpIndctn(self):
		return self._ModScpIndctn

	@ModScpIndctn.setter
	def ModScpIndctn(self, value):
		self._ModScpIndctn = value if type(value) != auto else self.make_default("ModScpIndctn")

	@ModScpIndctn.deleter
	def ModScpIndctn(self):
		del self._ModScpIndctn
		self._ModScpIndctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvstmtPlan', type=InvestmentPlan16, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModScpIndctn', type=DataModification1Code, min=1, max=1, mutex_group=None, array=False),
	))

