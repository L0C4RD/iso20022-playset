# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DataModification1Code import DataModification1Code
from ._SecuritiesAccountModification2Choice import SecuritiesAccountModification2Choice

class SecuritiesAccountModification2(base_types._BaseFieldType):

	__slots__ = ["_ReqdMod", "_ScpIndctn"]
	@property
	def ReqdMod(self):
		return self._ReqdMod

	@ReqdMod.setter
	def ReqdMod(self, value):
		self._ReqdMod = value if type(value) != base_types.auto else self.make_default("ReqdMod")

	@ReqdMod.deleter
	def ReqdMod(self):
		del self._ReqdMod
		self._ReqdMod = None

	@property
	def ScpIndctn(self):
		return self._ScpIndctn

	@ScpIndctn.setter
	def ScpIndctn(self, value):
		self._ScpIndctn = value if type(value) != base_types.auto else self.make_default("ScpIndctn")

	@ScpIndctn.deleter
	def ScpIndctn(self):
		del self._ScpIndctn
		self._ScpIndctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqdMod', type=SecuritiesAccountModification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScpIndctn', type=DataModification1Code, min=1, max=1, mutex_group=None, array=False),
	))