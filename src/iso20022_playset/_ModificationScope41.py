# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DataModification1Code
from . import InvestmentPlan16

class ModificationScope41(base_types._BaseFieldType):

	__slots__ = ["_InvstmtPlan", "_ModScpIndctn"]
	@property
	def InvstmtPlan(self):
		return self._InvstmtPlan

	@InvstmtPlan.setter
	def InvstmtPlan(self, value):
		self._InvstmtPlan = value if value is not None else base_types.UninitialisedField(self, 'InvstmtPlan', InvestmentPlan16, False)

	@InvstmtPlan.deleter
	def InvstmtPlan(self):
		del self._InvstmtPlan
		self._InvstmtPlan = base_types.UninitialisedField(self, 'InvstmtPlan', InvestmentPlan16, False)

	@property
	def ModScpIndctn(self):
		return self._ModScpIndctn

	@ModScpIndctn.setter
	def ModScpIndctn(self, value):
		self._ModScpIndctn = value if value is not None else base_types.UninitialisedField(self, 'ModScpIndctn', DataModification1Code, False)

	@ModScpIndctn.deleter
	def ModScpIndctn(self):
		del self._ModScpIndctn
		self._ModScpIndctn = base_types.UninitialisedField(self, 'ModScpIndctn', DataModification1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvstmtPlan', type=InvestmentPlan16, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModScpIndctn', type=DataModification1Code, min=1, max=1, mutex_group=None, array=False),
	))