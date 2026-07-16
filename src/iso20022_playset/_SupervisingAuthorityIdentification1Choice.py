# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExternalAuthorityIdentification1Code
from . import Max350Text

class SupervisingAuthorityIdentification1Choice(base_types._BaseFieldType):

	__slots__ = ["_FullNm", "_PrtryId"]
	@property
	def FullNm(self):
		return self._FullNm

	@FullNm.setter
	def FullNm(self, value):
		self._FullNm = value if value is not None else base_types.UninitialisedField(self, 'FullNm', Max350Text, False)

	@FullNm.deleter
	def FullNm(self):
		del self._FullNm
		self._FullNm = base_types.UninitialisedField(self, 'FullNm', Max350Text, False)

	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if value is not None else base_types.UninitialisedField(self, 'PrtryId', ExternalAuthorityIdentification1Code, False)

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = base_types.UninitialisedField(self, 'PrtryId', ExternalAuthorityIdentification1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FullNm', type=Max350Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryId', type=ExternalAuthorityIdentification1Code, min=0, max=1, mutex_group=1, array=False),
	))