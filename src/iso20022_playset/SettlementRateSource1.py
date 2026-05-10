from . import base_types
import Exact4NumericText
import CountryCode
import RateSourceText
import Exact2AlphaNumericText

class SettlementRateSource1(base_types._BaseFieldType):

	__slots__ = ["_LctnCd", "_Tm", "_RateSrc", "_CtryCd"]
	@property
	def LctnCd(self):
		return self._LctnCd

	@LctnCd.setter
	def LctnCd(self, value):
		self._LctnCd = value if type(value) != auto else self.make_default("LctnCd")

	@LctnCd.deleter
	def LctnCd(self):
		del self._LctnCd
		self._LctnCd = None

	@property
	def Tm(self):
		return self._Tm

	@Tm.setter
	def Tm(self, value):
		self._Tm = value if type(value) != auto else self.make_default("Tm")

	@Tm.deleter
	def Tm(self):
		del self._Tm
		self._Tm = None

	@property
	def RateSrc(self):
		return self._RateSrc

	@RateSrc.setter
	def RateSrc(self, value):
		self._RateSrc = value if type(value) != auto else self.make_default("RateSrc")

	@RateSrc.deleter
	def RateSrc(self):
		del self._RateSrc
		self._RateSrc = None

	@property
	def CtryCd(self):
		return self._CtryCd

	@CtryCd.setter
	def CtryCd(self, value):
		self._CtryCd = value if type(value) != auto else self.make_default("CtryCd")

	@CtryCd.deleter
	def CtryCd(self):
		del self._CtryCd
		self._CtryCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LctnCd', type=Exact2AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tm', type=Exact4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateSrc', type=RateSourceText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryCd', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
	))

