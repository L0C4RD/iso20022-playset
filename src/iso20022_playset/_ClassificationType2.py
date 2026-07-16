# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CFIOct2015Identifier
from . import ExternalFinancialInstrumentProductType1Code
from . import GenericIdentification36

class ClassificationType2(base_types._BaseFieldType):

	__slots__ = ["_AltrnClssfctn", "_ClssfctnFinInstrm", "_FinInstrmPdctTpCd"]
	@property
	def AltrnClssfctn(self):
		return self._AltrnClssfctn

	@AltrnClssfctn.setter
	def AltrnClssfctn(self, value):
		self._AltrnClssfctn = value if value is not None else base_types.UninitialisedField(self, 'AltrnClssfctn', GenericIdentification36, True)

	@AltrnClssfctn.deleter
	def AltrnClssfctn(self):
		del self._AltrnClssfctn
		self._AltrnClssfctn = base_types.UninitialisedField(self, 'AltrnClssfctn', GenericIdentification36, True)

	@property
	def ClssfctnFinInstrm(self):
		return self._ClssfctnFinInstrm

	@ClssfctnFinInstrm.setter
	def ClssfctnFinInstrm(self, value):
		self._ClssfctnFinInstrm = value if value is not None else base_types.UninitialisedField(self, 'ClssfctnFinInstrm', CFIOct2015Identifier, False)

	@ClssfctnFinInstrm.deleter
	def ClssfctnFinInstrm(self):
		del self._ClssfctnFinInstrm
		self._ClssfctnFinInstrm = base_types.UninitialisedField(self, 'ClssfctnFinInstrm', CFIOct2015Identifier, False)

	@property
	def FinInstrmPdctTpCd(self):
		return self._FinInstrmPdctTpCd

	@FinInstrmPdctTpCd.setter
	def FinInstrmPdctTpCd(self, value):
		self._FinInstrmPdctTpCd = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmPdctTpCd', ExternalFinancialInstrumentProductType1Code, False)

	@FinInstrmPdctTpCd.deleter
	def FinInstrmPdctTpCd(self):
		del self._FinInstrmPdctTpCd
		self._FinInstrmPdctTpCd = base_types.UninitialisedField(self, 'FinInstrmPdctTpCd', ExternalFinancialInstrumentProductType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrnClssfctn', type=GenericIdentification36, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClssfctnFinInstrm', type=CFIOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmPdctTpCd', type=ExternalFinancialInstrumentProductType1Code, min=0, max=1, mutex_group=None, array=False),
	))