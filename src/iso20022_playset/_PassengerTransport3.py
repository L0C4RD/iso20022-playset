# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import AmountDetails3
from . import AncillaryPurchase3
from . import Customer9
from . import CustomerReference1
from . import DepartureOrArrival1
from . import HiredVehicle3
from . import LoyaltyProgramme4
from . import Max35Text
from . import Max4NumericText
from . import Max4Text
from . import Max70Text
from . import TripLeg3
from . import TrueFalseIndicator

class PassengerTransport3(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_AncllryPurchs", "_CstmrRef", "_DocNb", "_Dprture", "_Drtn", "_HirdVhclDtls", "_Insrnc", "_LltyPrgrmm", "_OpnTckt", "_OrgnlRsvatnNb", "_OrgnlRsvatnSys", "_Pssngr", "_RsvatnNb", "_RsvatnSys", "_SummryCmmdtyId", "_TcktIssr", "_TripLeg", "_TrvlAuthstnCd", "_TtlAmt"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@property
	def AncllryPurchs(self):
		return self._AncllryPurchs

	@AncllryPurchs.setter
	def AncllryPurchs(self, value):
		self._AncllryPurchs = value if value is not None else base_types.UninitialisedField(self, 'AncllryPurchs', AncillaryPurchase3, True)

	@AncllryPurchs.deleter
	def AncllryPurchs(self):
		del self._AncllryPurchs
		self._AncllryPurchs = base_types.UninitialisedField(self, 'AncllryPurchs', AncillaryPurchase3, True)

	@property
	def CstmrRef(self):
		return self._CstmrRef

	@CstmrRef.setter
	def CstmrRef(self, value):
		self._CstmrRef = value if value is not None else base_types.UninitialisedField(self, 'CstmrRef', CustomerReference1, True)

	@CstmrRef.deleter
	def CstmrRef(self):
		del self._CstmrRef
		self._CstmrRef = base_types.UninitialisedField(self, 'CstmrRef', CustomerReference1, True)

	@property
	def DocNb(self):
		return self._DocNb

	@DocNb.setter
	def DocNb(self, value):
		self._DocNb = value if value is not None else base_types.UninitialisedField(self, 'DocNb', Max35Text, False)

	@DocNb.deleter
	def DocNb(self):
		del self._DocNb
		self._DocNb = base_types.UninitialisedField(self, 'DocNb', Max35Text, False)

	@property
	def Dprture(self):
		return self._Dprture

	@Dprture.setter
	def Dprture(self, value):
		self._Dprture = value if value is not None else base_types.UninitialisedField(self, 'Dprture', DepartureOrArrival1, False)

	@Dprture.deleter
	def Dprture(self):
		del self._Dprture
		self._Dprture = base_types.UninitialisedField(self, 'Dprture', DepartureOrArrival1, False)

	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if value is not None else base_types.UninitialisedField(self, 'Drtn', Max4NumericText, False)

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = base_types.UninitialisedField(self, 'Drtn', Max4NumericText, False)

	@property
	def HirdVhclDtls(self):
		return self._HirdVhclDtls

	@HirdVhclDtls.setter
	def HirdVhclDtls(self, value):
		self._HirdVhclDtls = value if value is not None else base_types.UninitialisedField(self, 'HirdVhclDtls', HiredVehicle3, True)

	@HirdVhclDtls.deleter
	def HirdVhclDtls(self):
		del self._HirdVhclDtls
		self._HirdVhclDtls = base_types.UninitialisedField(self, 'HirdVhclDtls', HiredVehicle3, True)

	@property
	def Insrnc(self):
		return self._Insrnc

	@Insrnc.setter
	def Insrnc(self, value):
		self._Insrnc = value if value is not None else base_types.UninitialisedField(self, 'Insrnc', TrueFalseIndicator, False)

	@Insrnc.deleter
	def Insrnc(self):
		del self._Insrnc
		self._Insrnc = base_types.UninitialisedField(self, 'Insrnc', TrueFalseIndicator, False)

	@property
	def LltyPrgrmm(self):
		return self._LltyPrgrmm

	@LltyPrgrmm.setter
	def LltyPrgrmm(self, value):
		self._LltyPrgrmm = value if value is not None else base_types.UninitialisedField(self, 'LltyPrgrmm', LoyaltyProgramme4, False)

	@LltyPrgrmm.deleter
	def LltyPrgrmm(self):
		del self._LltyPrgrmm
		self._LltyPrgrmm = base_types.UninitialisedField(self, 'LltyPrgrmm', LoyaltyProgramme4, False)

	@property
	def OpnTckt(self):
		return self._OpnTckt

	@OpnTckt.setter
	def OpnTckt(self, value):
		self._OpnTckt = value if value is not None else base_types.UninitialisedField(self, 'OpnTckt', TrueFalseIndicator, False)

	@OpnTckt.deleter
	def OpnTckt(self):
		del self._OpnTckt
		self._OpnTckt = base_types.UninitialisedField(self, 'OpnTckt', TrueFalseIndicator, False)

	@property
	def OrgnlRsvatnNb(self):
		return self._OrgnlRsvatnNb

	@OrgnlRsvatnNb.setter
	def OrgnlRsvatnNb(self, value):
		self._OrgnlRsvatnNb = value if value is not None else base_types.UninitialisedField(self, 'OrgnlRsvatnNb', Max35Text, False)

	@OrgnlRsvatnNb.deleter
	def OrgnlRsvatnNb(self):
		del self._OrgnlRsvatnNb
		self._OrgnlRsvatnNb = base_types.UninitialisedField(self, 'OrgnlRsvatnNb', Max35Text, False)

	@property
	def OrgnlRsvatnSys(self):
		return self._OrgnlRsvatnSys

	@OrgnlRsvatnSys.setter
	def OrgnlRsvatnSys(self, value):
		self._OrgnlRsvatnSys = value if value is not None else base_types.UninitialisedField(self, 'OrgnlRsvatnSys', Max4Text, False)

	@OrgnlRsvatnSys.deleter
	def OrgnlRsvatnSys(self):
		del self._OrgnlRsvatnSys
		self._OrgnlRsvatnSys = base_types.UninitialisedField(self, 'OrgnlRsvatnSys', Max4Text, False)

	@property
	def Pssngr(self):
		return self._Pssngr

	@Pssngr.setter
	def Pssngr(self, value):
		self._Pssngr = value if value is not None else base_types.UninitialisedField(self, 'Pssngr', Customer9, True)

	@Pssngr.deleter
	def Pssngr(self):
		del self._Pssngr
		self._Pssngr = base_types.UninitialisedField(self, 'Pssngr', Customer9, True)

	@property
	def RsvatnNb(self):
		return self._RsvatnNb

	@RsvatnNb.setter
	def RsvatnNb(self, value):
		self._RsvatnNb = value if value is not None else base_types.UninitialisedField(self, 'RsvatnNb', Max35Text, False)

	@RsvatnNb.deleter
	def RsvatnNb(self):
		del self._RsvatnNb
		self._RsvatnNb = base_types.UninitialisedField(self, 'RsvatnNb', Max35Text, False)

	@property
	def RsvatnSys(self):
		return self._RsvatnSys

	@RsvatnSys.setter
	def RsvatnSys(self, value):
		self._RsvatnSys = value if value is not None else base_types.UninitialisedField(self, 'RsvatnSys', Max4Text, False)

	@RsvatnSys.deleter
	def RsvatnSys(self):
		del self._RsvatnSys
		self._RsvatnSys = base_types.UninitialisedField(self, 'RsvatnSys', Max4Text, False)

	@property
	def SummryCmmdtyId(self):
		return self._SummryCmmdtyId

	@SummryCmmdtyId.setter
	def SummryCmmdtyId(self, value):
		self._SummryCmmdtyId = value if value is not None else base_types.UninitialisedField(self, 'SummryCmmdtyId', Max35Text, False)

	@SummryCmmdtyId.deleter
	def SummryCmmdtyId(self):
		del self._SummryCmmdtyId
		self._SummryCmmdtyId = base_types.UninitialisedField(self, 'SummryCmmdtyId', Max35Text, False)

	@property
	def TcktIssr(self):
		return self._TcktIssr

	@TcktIssr.setter
	def TcktIssr(self, value):
		self._TcktIssr = value if value is not None else base_types.UninitialisedField(self, 'TcktIssr', Max35Text, False)

	@TcktIssr.deleter
	def TcktIssr(self):
		del self._TcktIssr
		self._TcktIssr = base_types.UninitialisedField(self, 'TcktIssr', Max35Text, False)

	@property
	def TripLeg(self):
		return self._TripLeg

	@TripLeg.setter
	def TripLeg(self, value):
		self._TripLeg = value if value is not None else base_types.UninitialisedField(self, 'TripLeg', TripLeg3, True)

	@TripLeg.deleter
	def TripLeg(self):
		del self._TripLeg
		self._TripLeg = base_types.UninitialisedField(self, 'TripLeg', TripLeg3, True)

	@property
	def TrvlAuthstnCd(self):
		return self._TrvlAuthstnCd

	@TrvlAuthstnCd.setter
	def TrvlAuthstnCd(self, value):
		self._TrvlAuthstnCd = value if value is not None else base_types.UninitialisedField(self, 'TrvlAuthstnCd', Max70Text, False)

	@TrvlAuthstnCd.deleter
	def TrvlAuthstnCd(self):
		del self._TrvlAuthstnCd
		self._TrvlAuthstnCd = base_types.UninitialisedField(self, 'TrvlAuthstnCd', Max70Text, False)

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAmt', AmountDetails3, True)

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = base_types.UninitialisedField(self, 'TtlAmt', AmountDetails3, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AncllryPurchs', type=AncillaryPurchase3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CstmrRef', type=CustomerReference1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DocNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dprture', type=DepartureOrArrival1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drtn', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HirdVhclDtls', type=HiredVehicle3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Insrnc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyPrgrmm', type=LoyaltyProgramme4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpnTckt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlRsvatnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlRsvatnSys', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pssngr', type=Customer9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RsvatnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsvatnSys', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TcktIssr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripLeg', type=TripLeg3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrvlAuthstnCd', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=AmountDetails3, min=0, max=None, mutex_group=None, array=True),
	))