# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import DistributionPolicy1Code
from . import FormOfSecurity1Code
from . import Max140Text
from . import Max350Text
from . import Max35Text
from . import SecurityIdentification46Choice
from . import Series1
from . import YesNoIndicator

class FinancialInstrument106(base_types._BaseFieldType):

	__slots__ = ["_ClssTp", "_DnmtnCcy", "_DstrbtnPlcy", "_DualFndInd", "_Id", "_Nm", "_PdctGrp", "_SctiesForm", "_ShrtNm", "_SplmtryId", "_SrsId"]
	@property
	def ClssTp(self):
		return self._ClssTp

	@ClssTp.setter
	def ClssTp(self, value):
		self._ClssTp = value if value is not None else base_types.UninitialisedField(self, 'ClssTp', Max35Text, False)

	@ClssTp.deleter
	def ClssTp(self):
		del self._ClssTp
		self._ClssTp = base_types.UninitialisedField(self, 'ClssTp', Max35Text, False)

	@property
	def DnmtnCcy(self):
		return self._DnmtnCcy

	@DnmtnCcy.setter
	def DnmtnCcy(self, value):
		self._DnmtnCcy = value if value is not None else base_types.UninitialisedField(self, 'DnmtnCcy', ActiveOrHistoricCurrencyCode, False)

	@DnmtnCcy.deleter
	def DnmtnCcy(self):
		del self._DnmtnCcy
		self._DnmtnCcy = base_types.UninitialisedField(self, 'DnmtnCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def DstrbtnPlcy(self):
		return self._DstrbtnPlcy

	@DstrbtnPlcy.setter
	def DstrbtnPlcy(self, value):
		self._DstrbtnPlcy = value if value is not None else base_types.UninitialisedField(self, 'DstrbtnPlcy', DistributionPolicy1Code, False)

	@DstrbtnPlcy.deleter
	def DstrbtnPlcy(self):
		del self._DstrbtnPlcy
		self._DstrbtnPlcy = base_types.UninitialisedField(self, 'DstrbtnPlcy', DistributionPolicy1Code, False)

	@property
	def DualFndInd(self):
		return self._DualFndInd

	@DualFndInd.setter
	def DualFndInd(self, value):
		self._DualFndInd = value if value is not None else base_types.UninitialisedField(self, 'DualFndInd', YesNoIndicator, False)

	@DualFndInd.deleter
	def DualFndInd(self):
		del self._DualFndInd
		self._DualFndInd = base_types.UninitialisedField(self, 'DualFndInd', YesNoIndicator, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', SecurityIdentification46Choice, True)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', SecurityIdentification46Choice, True)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max350Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max350Text, False)

	@property
	def PdctGrp(self):
		return self._PdctGrp

	@PdctGrp.setter
	def PdctGrp(self, value):
		self._PdctGrp = value if value is not None else base_types.UninitialisedField(self, 'PdctGrp', Max140Text, False)

	@PdctGrp.deleter
	def PdctGrp(self):
		del self._PdctGrp
		self._PdctGrp = base_types.UninitialisedField(self, 'PdctGrp', Max140Text, False)

	@property
	def SctiesForm(self):
		return self._SctiesForm

	@SctiesForm.setter
	def SctiesForm(self, value):
		self._SctiesForm = value if value is not None else base_types.UninitialisedField(self, 'SctiesForm', FormOfSecurity1Code, False)

	@SctiesForm.deleter
	def SctiesForm(self):
		del self._SctiesForm
		self._SctiesForm = base_types.UninitialisedField(self, 'SctiesForm', FormOfSecurity1Code, False)

	@property
	def ShrtNm(self):
		return self._ShrtNm

	@ShrtNm.setter
	def ShrtNm(self, value):
		self._ShrtNm = value if value is not None else base_types.UninitialisedField(self, 'ShrtNm', Max35Text, False)

	@ShrtNm.deleter
	def ShrtNm(self):
		del self._ShrtNm
		self._ShrtNm = base_types.UninitialisedField(self, 'ShrtNm', Max35Text, False)

	@property
	def SplmtryId(self):
		return self._SplmtryId

	@SplmtryId.setter
	def SplmtryId(self, value):
		self._SplmtryId = value if value is not None else base_types.UninitialisedField(self, 'SplmtryId', Max35Text, False)

	@SplmtryId.deleter
	def SplmtryId(self):
		del self._SplmtryId
		self._SplmtryId = base_types.UninitialisedField(self, 'SplmtryId', Max35Text, False)

	@property
	def SrsId(self):
		return self._SrsId

	@SrsId.setter
	def SrsId(self, value):
		self._SrsId = value if value is not None else base_types.UninitialisedField(self, 'SrsId', Series1, False)

	@SrsId.deleter
	def SrsId(self):
		del self._SrsId
		self._SrsId = base_types.UninitialisedField(self, 'SrsId', Series1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DnmtnCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstrbtnPlcy', type=DistributionPolicy1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DualFndInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=SecurityIdentification46Choice, min=1, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctGrp', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesForm', type=FormOfSecurity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrsId', type=Series1, min=0, max=1, mutex_group=None, array=False),
	))