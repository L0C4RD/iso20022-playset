from . import base_types
from .Max350Text import Max350Text
from .ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from .ISINOct2015Identifier import ISINOct2015Identifier
from .TrueFalseIndicator import TrueFalseIndicator
from .CFIOct2015Identifier import CFIOct2015Identifier
from .Max35Text import Max35Text

class SecurityInstrumentDescription9(base_types._BaseFieldType):

	__slots__ = ["_NtnlCcy", "_CmmdtyDerivInd", "_FullNm", "_ShrtNm", "_ClssfctnTp", "_Id"]
	@property
	def NtnlCcy(self):
		return self._NtnlCcy

	@NtnlCcy.setter
	def NtnlCcy(self, value):
		self._NtnlCcy = value if type(value) != base_types.auto else self.make_default("NtnlCcy")

	@NtnlCcy.deleter
	def NtnlCcy(self):
		del self._NtnlCcy
		self._NtnlCcy = None

	@property
	def CmmdtyDerivInd(self):
		return self._CmmdtyDerivInd

	@CmmdtyDerivInd.setter
	def CmmdtyDerivInd(self, value):
		self._CmmdtyDerivInd = value if type(value) != base_types.auto else self.make_default("CmmdtyDerivInd")

	@CmmdtyDerivInd.deleter
	def CmmdtyDerivInd(self):
		del self._CmmdtyDerivInd
		self._CmmdtyDerivInd = None

	@property
	def FullNm(self):
		return self._FullNm

	@FullNm.setter
	def FullNm(self, value):
		self._FullNm = value if type(value) != base_types.auto else self.make_default("FullNm")

	@FullNm.deleter
	def FullNm(self):
		del self._FullNm
		self._FullNm = None

	@property
	def ShrtNm(self):
		return self._ShrtNm

	@ShrtNm.setter
	def ShrtNm(self, value):
		self._ShrtNm = value if type(value) != base_types.auto else self.make_default("ShrtNm")

	@ShrtNm.deleter
	def ShrtNm(self):
		del self._ShrtNm
		self._ShrtNm = None

	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if type(value) != base_types.auto else self.make_default("ClssfctnTp")

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtnlCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmmdtyDerivInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullNm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssfctnTp', type=CFIOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
	))

