# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Modification1Code
from . import Restriction1

class RestrictionModification1(base_types._BaseFieldType):

	__slots__ = ["_ModCd", "_Rstrctn"]
	@property
	def ModCd(self):
		return self._ModCd

	@ModCd.setter
	def ModCd(self, value):
		self._ModCd = value if value is not None else base_types.UninitialisedField(self, 'ModCd', Modification1Code, False)

	@ModCd.deleter
	def ModCd(self):
		del self._ModCd
		self._ModCd = base_types.UninitialisedField(self, 'ModCd', Modification1Code, False)

	@property
	def Rstrctn(self):
		return self._Rstrctn

	@Rstrctn.setter
	def Rstrctn(self, value):
		self._Rstrctn = value if value is not None else base_types.UninitialisedField(self, 'Rstrctn', Restriction1, False)

	@Rstrctn.deleter
	def Rstrctn(self):
		del self._Rstrctn
		self._Rstrctn = base_types.UninitialisedField(self, 'Rstrctn', Restriction1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ModCd', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rstrctn', type=Restriction1, min=1, max=1, mutex_group=None, array=False),
	))