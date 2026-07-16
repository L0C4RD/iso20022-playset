# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text
from . import Modification1Code

class FullLegalNameModification1(base_types._BaseFieldType):

	__slots__ = ["_FullLglNm", "_ModCd"]
	@property
	def FullLglNm(self):
		return self._FullLglNm

	@FullLglNm.setter
	def FullLglNm(self, value):
		self._FullLglNm = value if value is not None else base_types.UninitialisedField(self, 'FullLglNm', Max350Text, False)

	@FullLglNm.deleter
	def FullLglNm(self):
		del self._FullLglNm
		self._FullLglNm = base_types.UninitialisedField(self, 'FullLglNm', Max350Text, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='FullLglNm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModCd', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
	))