# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max1025Text
from . import Max256Text
from . import Max35Text
from . import Max8Text
from . import Organisation26
from . import RetailerMessage1Code
from . import RetailerService2Code
from . import RetailerService8Code
from . import TerminalManagementAction3Code

class SaleToPOIProtocolParameter4(base_types._BaseFieldType):

	__slots__ = ["_ActnTp", "_AllwdPOIMsg", "_AllwdPOISvc", "_AllwdSaleDvc", "_AllwdSaleMsg", "_HstId", "_MrchntId", "_MrchntPOIId", "_PrtcolVrsn", "_SaleId", "_Vrsn", "_XtrnlyTpSpprtd"]
	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if value is not None else base_types.UninitialisedField(self, 'ActnTp', TerminalManagementAction3Code, False)

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = base_types.UninitialisedField(self, 'ActnTp', TerminalManagementAction3Code, False)

	@property
	def AllwdPOIMsg(self):
		return self._AllwdPOIMsg

	@AllwdPOIMsg.setter
	def AllwdPOIMsg(self, value):
		self._AllwdPOIMsg = value if value is not None else base_types.UninitialisedField(self, 'AllwdPOIMsg', RetailerMessage1Code, True)

	@AllwdPOIMsg.deleter
	def AllwdPOIMsg(self):
		del self._AllwdPOIMsg
		self._AllwdPOIMsg = base_types.UninitialisedField(self, 'AllwdPOIMsg', RetailerMessage1Code, True)

	@property
	def AllwdPOISvc(self):
		return self._AllwdPOISvc

	@AllwdPOISvc.setter
	def AllwdPOISvc(self, value):
		self._AllwdPOISvc = value if value is not None else base_types.UninitialisedField(self, 'AllwdPOISvc', RetailerService2Code, True)

	@AllwdPOISvc.deleter
	def AllwdPOISvc(self):
		del self._AllwdPOISvc
		self._AllwdPOISvc = base_types.UninitialisedField(self, 'AllwdPOISvc', RetailerService2Code, True)

	@property
	def AllwdSaleDvc(self):
		return self._AllwdSaleDvc

	@AllwdSaleDvc.setter
	def AllwdSaleDvc(self, value):
		self._AllwdSaleDvc = value if value is not None else base_types.UninitialisedField(self, 'AllwdSaleDvc', RetailerService8Code, True)

	@AllwdSaleDvc.deleter
	def AllwdSaleDvc(self):
		del self._AllwdSaleDvc
		self._AllwdSaleDvc = base_types.UninitialisedField(self, 'AllwdSaleDvc', RetailerService8Code, True)

	@property
	def AllwdSaleMsg(self):
		return self._AllwdSaleMsg

	@AllwdSaleMsg.setter
	def AllwdSaleMsg(self, value):
		self._AllwdSaleMsg = value if value is not None else base_types.UninitialisedField(self, 'AllwdSaleMsg', RetailerMessage1Code, True)

	@AllwdSaleMsg.deleter
	def AllwdSaleMsg(self):
		del self._AllwdSaleMsg
		self._AllwdSaleMsg = base_types.UninitialisedField(self, 'AllwdSaleMsg', RetailerMessage1Code, True)

	@property
	def HstId(self):
		return self._HstId

	@HstId.setter
	def HstId(self, value):
		self._HstId = value if value is not None else base_types.UninitialisedField(self, 'HstId', Max35Text, False)

	@HstId.deleter
	def HstId(self):
		del self._HstId
		self._HstId = base_types.UninitialisedField(self, 'HstId', Max35Text, False)

	@property
	def MrchntId(self):
		return self._MrchntId

	@MrchntId.setter
	def MrchntId(self, value):
		self._MrchntId = value if value is not None else base_types.UninitialisedField(self, 'MrchntId', Organisation26, False)

	@MrchntId.deleter
	def MrchntId(self):
		del self._MrchntId
		self._MrchntId = base_types.UninitialisedField(self, 'MrchntId', Organisation26, False)

	@property
	def MrchntPOIId(self):
		return self._MrchntPOIId

	@MrchntPOIId.setter
	def MrchntPOIId(self, value):
		self._MrchntPOIId = value if value is not None else base_types.UninitialisedField(self, 'MrchntPOIId', Max35Text, False)

	@MrchntPOIId.deleter
	def MrchntPOIId(self):
		del self._MrchntPOIId
		self._MrchntPOIId = base_types.UninitialisedField(self, 'MrchntPOIId', Max35Text, False)

	@property
	def PrtcolVrsn(self):
		return self._PrtcolVrsn

	@PrtcolVrsn.setter
	def PrtcolVrsn(self, value):
		self._PrtcolVrsn = value if value is not None else base_types.UninitialisedField(self, 'PrtcolVrsn', Max8Text, False)

	@PrtcolVrsn.deleter
	def PrtcolVrsn(self):
		del self._PrtcolVrsn
		self._PrtcolVrsn = base_types.UninitialisedField(self, 'PrtcolVrsn', Max8Text, False)

	@property
	def SaleId(self):
		return self._SaleId

	@SaleId.setter
	def SaleId(self, value):
		self._SaleId = value if value is not None else base_types.UninitialisedField(self, 'SaleId', Max35Text, False)

	@SaleId.deleter
	def SaleId(self):
		del self._SaleId
		self._SaleId = base_types.UninitialisedField(self, 'SaleId', Max35Text, False)

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', Max256Text, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', Max256Text, False)

	@property
	def XtrnlyTpSpprtd(self):
		return self._XtrnlyTpSpprtd

	@XtrnlyTpSpprtd.setter
	def XtrnlyTpSpprtd(self, value):
		self._XtrnlyTpSpprtd = value if value is not None else base_types.UninitialisedField(self, 'XtrnlyTpSpprtd', Max1025Text, True)

	@XtrnlyTpSpprtd.deleter
	def XtrnlyTpSpprtd(self):
		del self._XtrnlyTpSpprtd
		self._XtrnlyTpSpprtd = base_types.UninitialisedField(self, 'XtrnlyTpSpprtd', Max1025Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnTp', type=TerminalManagementAction3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AllwdPOIMsg', type=RetailerMessage1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AllwdPOISvc', type=RetailerService2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AllwdSaleDvc', type=RetailerService8Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AllwdSaleMsg', type=RetailerMessage1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='HstId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntId', type=Organisation26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntPOIId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtcolVrsn', type=Max8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtrnlyTpSpprtd', type=Max1025Text, min=0, max=None, mutex_group=None, array=True),
	))