# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DataModification2Code
from . import PartyProfileInformation5

class ModificationScope27(base_types._BaseFieldType):

	__slots__ = ["_InvstrPrflVldtn", "_ModScpIndctn"]
	@property
	def InvstrPrflVldtn(self):
		return self._InvstrPrflVldtn

	@InvstrPrflVldtn.setter
	def InvstrPrflVldtn(self, value):
		self._InvstrPrflVldtn = value if value is not None else base_types.UninitialisedField(self, 'InvstrPrflVldtn', PartyProfileInformation5, False)

	@InvstrPrflVldtn.deleter
	def InvstrPrflVldtn(self):
		del self._InvstrPrflVldtn
		self._InvstrPrflVldtn = base_types.UninitialisedField(self, 'InvstrPrflVldtn', PartyProfileInformation5, False)

	@property
	def ModScpIndctn(self):
		return self._ModScpIndctn

	@ModScpIndctn.setter
	def ModScpIndctn(self, value):
		self._ModScpIndctn = value if value is not None else base_types.UninitialisedField(self, 'ModScpIndctn', DataModification2Code, False)

	@ModScpIndctn.deleter
	def ModScpIndctn(self):
		del self._ModScpIndctn
		self._ModScpIndctn = base_types.UninitialisedField(self, 'ModScpIndctn', DataModification2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvstrPrflVldtn', type=PartyProfileInformation5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModScpIndctn', type=DataModification2Code, min=1, max=1, mutex_group=None, array=False),
	))