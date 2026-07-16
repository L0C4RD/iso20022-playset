# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PersonIdentificationSchemeName1Choice
from . import RequestedIndicator

class GenericPersonType1(base_types._BaseFieldType):

	__slots__ = ["_Reqd", "_SchmeNm"]
	@property
	def Reqd(self):
		return self._Reqd

	@Reqd.setter
	def Reqd(self, value):
		self._Reqd = value if value is not None else base_types.UninitialisedField(self, 'Reqd', RequestedIndicator, False)

	@Reqd.deleter
	def Reqd(self):
		del self._Reqd
		self._Reqd = base_types.UninitialisedField(self, 'Reqd', RequestedIndicator, False)

	@property
	def SchmeNm(self):
		return self._SchmeNm

	@SchmeNm.setter
	def SchmeNm(self, value):
		self._SchmeNm = value if value is not None else base_types.UninitialisedField(self, 'SchmeNm', PersonIdentificationSchemeName1Choice, False)

	@SchmeNm.deleter
	def SchmeNm(self):
		del self._SchmeNm
		self._SchmeNm = base_types.UninitialisedField(self, 'SchmeNm', PersonIdentificationSchemeName1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Reqd', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchmeNm', type=PersonIdentificationSchemeName1Choice, min=1, max=1, mutex_group=None, array=False),
	))