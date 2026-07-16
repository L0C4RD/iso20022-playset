# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DataModification1Code
from . import SecuritiesAccountModification2Choice

class SecuritiesAccountModification2(base_types._BaseFieldType):

	__slots__ = ["_ReqdMod", "_ScpIndctn"]
	@property
	def ReqdMod(self):
		return self._ReqdMod

	@ReqdMod.setter
	def ReqdMod(self, value):
		self._ReqdMod = value if value is not None else base_types.UninitialisedField(self, 'ReqdMod', SecuritiesAccountModification2Choice, False)

	@ReqdMod.deleter
	def ReqdMod(self):
		del self._ReqdMod
		self._ReqdMod = base_types.UninitialisedField(self, 'ReqdMod', SecuritiesAccountModification2Choice, False)

	@property
	def ScpIndctn(self):
		return self._ScpIndctn

	@ScpIndctn.setter
	def ScpIndctn(self, value):
		self._ScpIndctn = value if value is not None else base_types.UninitialisedField(self, 'ScpIndctn', DataModification1Code, False)

	@ScpIndctn.deleter
	def ScpIndctn(self):
		del self._ScpIndctn
		self._ScpIndctn = base_types.UninitialisedField(self, 'ScpIndctn', DataModification1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqdMod', type=SecuritiesAccountModification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScpIndctn', type=DataModification1Code, min=1, max=1, mutex_group=None, array=False),
	))