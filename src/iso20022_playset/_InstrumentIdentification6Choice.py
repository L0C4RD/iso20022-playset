# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification184
from . import ISINOct2015Identifier
from . import Max52Text
from . import UniqueProductIdentifier1Choice

class InstrumentIdentification6Choice(base_types._BaseFieldType):

	__slots__ = ["_AltrntvInstrmId", "_ISIN", "_OthrId", "_UnqPdctIdr"]
	@property
	def AltrntvInstrmId(self):
		return self._AltrntvInstrmId

	@AltrntvInstrmId.setter
	def AltrntvInstrmId(self, value):
		self._AltrntvInstrmId = value if value is not None else base_types.UninitialisedField(self, 'AltrntvInstrmId', Max52Text, False)

	@AltrntvInstrmId.deleter
	def AltrntvInstrmId(self):
		del self._AltrntvInstrmId
		self._AltrntvInstrmId = base_types.UninitialisedField(self, 'AltrntvInstrmId', Max52Text, False)

	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if value is not None else base_types.UninitialisedField(self, 'ISIN', ISINOct2015Identifier, False)

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = base_types.UninitialisedField(self, 'ISIN', ISINOct2015Identifier, False)

	@property
	def OthrId(self):
		return self._OthrId

	@OthrId.setter
	def OthrId(self, value):
		self._OthrId = value if value is not None else base_types.UninitialisedField(self, 'OthrId', GenericIdentification184, False)

	@OthrId.deleter
	def OthrId(self):
		del self._OthrId
		self._OthrId = base_types.UninitialisedField(self, 'OthrId', GenericIdentification184, False)

	@property
	def UnqPdctIdr(self):
		return self._UnqPdctIdr

	@UnqPdctIdr.setter
	def UnqPdctIdr(self, value):
		self._UnqPdctIdr = value if value is not None else base_types.UninitialisedField(self, 'UnqPdctIdr', UniqueProductIdentifier1Choice, False)

	@UnqPdctIdr.deleter
	def UnqPdctIdr(self):
		del self._UnqPdctIdr
		self._UnqPdctIdr = base_types.UninitialisedField(self, 'UnqPdctIdr', UniqueProductIdentifier1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrntvInstrmId', type=Max52Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrId', type=GenericIdentification184, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UnqPdctIdr', type=UniqueProductIdentifier1Choice, min=0, max=1, mutex_group=1, array=False),
	))