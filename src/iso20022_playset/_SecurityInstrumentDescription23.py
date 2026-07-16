# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import CFIOct2015Identifier
from . import ISINOct2015Identifier
from . import Max350Text
from . import OtherIdentification1

class SecurityInstrumentDescription23(base_types._BaseFieldType):

	__slots__ = ["_ClssfctnTp", "_FullNm", "_Id", "_NtnlCcy", "_OthrId"]
	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if value is not None else base_types.UninitialisedField(self, 'ClssfctnTp', CFIOct2015Identifier, False)

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = base_types.UninitialisedField(self, 'ClssfctnTp', CFIOct2015Identifier, False)

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
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', ISINOct2015Identifier, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', ISINOct2015Identifier, False)

	@property
	def NtnlCcy(self):
		return self._NtnlCcy

	@NtnlCcy.setter
	def NtnlCcy(self, value):
		self._NtnlCcy = value if value is not None else base_types.UninitialisedField(self, 'NtnlCcy', ActiveOrHistoricCurrencyCode, False)

	@NtnlCcy.deleter
	def NtnlCcy(self):
		del self._NtnlCcy
		self._NtnlCcy = base_types.UninitialisedField(self, 'NtnlCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def OthrId(self):
		return self._OthrId

	@OthrId.setter
	def OthrId(self, value):
		self._OthrId = value if value is not None else base_types.UninitialisedField(self, 'OthrId', OtherIdentification1, True)

	@OthrId.deleter
	def OthrId(self):
		del self._OthrId
		self._OthrId = base_types.UninitialisedField(self, 'OthrId', OtherIdentification1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssfctnTp', type=CFIOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullNm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrId', type=OtherIdentification1, min=0, max=None, mutex_group=None, array=True),
	))