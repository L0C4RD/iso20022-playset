# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DataModification1Code
from . import InvestorProfile2

class ModificationScope46(base_types._BaseFieldType):

	__slots__ = ["_InvstrPrfl", "_ModScpIndctn"]
	@property
	def InvstrPrfl(self):
		return self._InvstrPrfl

	@InvstrPrfl.setter
	def InvstrPrfl(self, value):
		self._InvstrPrfl = value if value is not None else base_types.UninitialisedField(self, 'InvstrPrfl', InvestorProfile2, False)

	@InvstrPrfl.deleter
	def InvstrPrfl(self):
		del self._InvstrPrfl
		self._InvstrPrfl = base_types.UninitialisedField(self, 'InvstrPrfl', InvestorProfile2, False)

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
		base_types.FieldEntry(name='InvstrPrfl', type=InvestorProfile2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModScpIndctn', type=DataModification1Code, min=1, max=1, mutex_group=None, array=False),
	))