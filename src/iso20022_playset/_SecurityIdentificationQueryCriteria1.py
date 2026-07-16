# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISINOct2015Identifier
from . import Max52Text

class SecurityIdentificationQueryCriteria1(base_types._BaseFieldType):

	__slots__ = ["_AltrntvInstrmId", "_ISIN"]
	@property
	def AltrntvInstrmId(self):
		return self._AltrntvInstrmId

	@AltrntvInstrmId.setter
	def AltrntvInstrmId(self, value):
		self._AltrntvInstrmId = value if value is not None else base_types.UninitialisedField(self, 'AltrntvInstrmId', Max52Text, True)

	@AltrntvInstrmId.deleter
	def AltrntvInstrmId(self):
		del self._AltrntvInstrmId
		self._AltrntvInstrmId = base_types.UninitialisedField(self, 'AltrntvInstrmId', Max52Text, True)

	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if value is not None else base_types.UninitialisedField(self, 'ISIN', ISINOct2015Identifier, True)

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = base_types.UninitialisedField(self, 'ISIN', ISINOct2015Identifier, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrntvInstrmId', type=Max52Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=None, mutex_group=None, array=True),
	))