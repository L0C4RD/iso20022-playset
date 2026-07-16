# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISO8583MessageErrorCode
from . import Max2NumericText
from . import Max4000Text
from . import Max500Text

class ErrorDetails4(base_types._BaseFieldType):

	__slots__ = ["_DataElmtInErr", "_Desc", "_ErrCd", "_svrtyCd"]
	@property
	def DataElmtInErr(self):
		return self._DataElmtInErr

	@DataElmtInErr.setter
	def DataElmtInErr(self, value):
		self._DataElmtInErr = value if value is not None else base_types.UninitialisedField(self, 'DataElmtInErr', Max4000Text, True)

	@DataElmtInErr.deleter
	def DataElmtInErr(self):
		del self._DataElmtInErr
		self._DataElmtInErr = base_types.UninitialisedField(self, 'DataElmtInErr', Max4000Text, True)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max500Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max500Text, False)

	@property
	def ErrCd(self):
		return self._ErrCd

	@ErrCd.setter
	def ErrCd(self, value):
		self._ErrCd = value if value is not None else base_types.UninitialisedField(self, 'ErrCd', ISO8583MessageErrorCode, False)

	@ErrCd.deleter
	def ErrCd(self):
		del self._ErrCd
		self._ErrCd = base_types.UninitialisedField(self, 'ErrCd', ISO8583MessageErrorCode, False)

	@property
	def svrtyCd(self):
		return self._svrtyCd

	@svrtyCd.setter
	def svrtyCd(self, value):
		self._svrtyCd = value if value is not None else base_types.UninitialisedField(self, 'svrtyCd', Max2NumericText, False)

	@svrtyCd.deleter
	def svrtyCd(self):
		del self._svrtyCd
		self._svrtyCd = base_types.UninitialisedField(self, 'svrtyCd', Max2NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataElmtInErr', type=Max4000Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Desc', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ErrCd', type=ISO8583MessageErrorCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='svrtyCd', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
	))