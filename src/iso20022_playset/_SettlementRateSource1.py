# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import Exact2AlphaNumericText
from . import Exact4NumericText
from . import RateSourceText

class SettlementRateSource1(base_types._BaseFieldType):

	__slots__ = ["_CtryCd", "_LctnCd", "_RateSrc", "_Tm"]
	@property
	def CtryCd(self):
		return self._CtryCd

	@CtryCd.setter
	def CtryCd(self, value):
		self._CtryCd = value if value is not None else base_types.UninitialisedField(self, 'CtryCd', CountryCode, False)

	@CtryCd.deleter
	def CtryCd(self):
		del self._CtryCd
		self._CtryCd = base_types.UninitialisedField(self, 'CtryCd', CountryCode, False)

	@property
	def LctnCd(self):
		return self._LctnCd

	@LctnCd.setter
	def LctnCd(self, value):
		self._LctnCd = value if value is not None else base_types.UninitialisedField(self, 'LctnCd', Exact2AlphaNumericText, False)

	@LctnCd.deleter
	def LctnCd(self):
		del self._LctnCd
		self._LctnCd = base_types.UninitialisedField(self, 'LctnCd', Exact2AlphaNumericText, False)

	@property
	def RateSrc(self):
		return self._RateSrc

	@RateSrc.setter
	def RateSrc(self, value):
		self._RateSrc = value if value is not None else base_types.UninitialisedField(self, 'RateSrc', RateSourceText, False)

	@RateSrc.deleter
	def RateSrc(self):
		del self._RateSrc
		self._RateSrc = base_types.UninitialisedField(self, 'RateSrc', RateSourceText, False)

	@property
	def Tm(self):
		return self._Tm

	@Tm.setter
	def Tm(self, value):
		self._Tm = value if value is not None else base_types.UninitialisedField(self, 'Tm', Exact4NumericText, False)

	@Tm.deleter
	def Tm(self):
		del self._Tm
		self._Tm = base_types.UninitialisedField(self, 'Tm', Exact4NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtryCd', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LctnCd', type=Exact2AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateSrc', type=RateSourceText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tm', type=Exact4NumericText, min=0, max=1, mutex_group=None, array=False),
	))