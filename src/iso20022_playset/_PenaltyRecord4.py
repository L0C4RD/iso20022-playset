# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection5
from . import Number
from . import PenaltyCalculationMethod1Code
from . import PenaltyCalculationRecord1
from . import PenaltyIdentification1
from . import PenaltyStatus2
from . import PenaltyTransaction3
from . import PenaltyType1Code
from . import YesNoIndicator

class PenaltyRecord4(base_types._BaseFieldType):

	__slots__ = ["_ClctnData", "_ClctnMtd", "_CmptdAmt", "_Id", "_Inslvncy", "_NbOfDays", "_RltdTx", "_Sts", "_Tp"]
	@property
	def ClctnData(self):
		return self._ClctnData

	@ClctnData.setter
	def ClctnData(self, value):
		self._ClctnData = value if value is not None else base_types.UninitialisedField(self, 'ClctnData', PenaltyCalculationRecord1, True)

	@ClctnData.deleter
	def ClctnData(self):
		del self._ClctnData
		self._ClctnData = base_types.UninitialisedField(self, 'ClctnData', PenaltyCalculationRecord1, True)

	@property
	def ClctnMtd(self):
		return self._ClctnMtd

	@ClctnMtd.setter
	def ClctnMtd(self, value):
		self._ClctnMtd = value if value is not None else base_types.UninitialisedField(self, 'ClctnMtd', PenaltyCalculationMethod1Code, False)

	@ClctnMtd.deleter
	def ClctnMtd(self):
		del self._ClctnMtd
		self._ClctnMtd = base_types.UninitialisedField(self, 'ClctnMtd', PenaltyCalculationMethod1Code, False)

	@property
	def CmptdAmt(self):
		return self._CmptdAmt

	@CmptdAmt.setter
	def CmptdAmt(self, value):
		self._CmptdAmt = value if value is not None else base_types.UninitialisedField(self, 'CmptdAmt', AmountAndDirection5, False)

	@CmptdAmt.deleter
	def CmptdAmt(self):
		del self._CmptdAmt
		self._CmptdAmt = base_types.UninitialisedField(self, 'CmptdAmt', AmountAndDirection5, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PenaltyIdentification1, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PenaltyIdentification1, False)

	@property
	def Inslvncy(self):
		return self._Inslvncy

	@Inslvncy.setter
	def Inslvncy(self, value):
		self._Inslvncy = value if value is not None else base_types.UninitialisedField(self, 'Inslvncy', YesNoIndicator, False)

	@Inslvncy.deleter
	def Inslvncy(self):
		del self._Inslvncy
		self._Inslvncy = base_types.UninitialisedField(self, 'Inslvncy', YesNoIndicator, False)

	@property
	def NbOfDays(self):
		return self._NbOfDays

	@NbOfDays.setter
	def NbOfDays(self, value):
		self._NbOfDays = value if value is not None else base_types.UninitialisedField(self, 'NbOfDays', Number, False)

	@NbOfDays.deleter
	def NbOfDays(self):
		del self._NbOfDays
		self._NbOfDays = base_types.UninitialisedField(self, 'NbOfDays', Number, False)

	@property
	def RltdTx(self):
		return self._RltdTx

	@RltdTx.setter
	def RltdTx(self, value):
		self._RltdTx = value if value is not None else base_types.UninitialisedField(self, 'RltdTx', PenaltyTransaction3, False)

	@RltdTx.deleter
	def RltdTx(self):
		del self._RltdTx
		self._RltdTx = base_types.UninitialisedField(self, 'RltdTx', PenaltyTransaction3, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', PenaltyStatus2, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', PenaltyStatus2, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', PenaltyType1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', PenaltyType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClctnData', type=PenaltyCalculationRecord1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClctnMtd', type=PenaltyCalculationMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmptdAmt', type=AmountAndDirection5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PenaltyIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Inslvncy', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDays', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdTx', type=PenaltyTransaction3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=PenaltyStatus2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=PenaltyType1Code, min=1, max=1, mutex_group=None, array=False),
	))