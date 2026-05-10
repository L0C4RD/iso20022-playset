from . import base_types
from ._Max4Text import Max4Text
from ._Customer9 import Customer9
from ._TripLeg3 import TripLeg3
from ._Max4NumericText import Max4NumericText
from ._Max70Text import Max70Text
from ._CustomerReference1 import CustomerReference1
from ._DepartureOrArrival1 import DepartureOrArrival1
from ._AmountDetails3 import AmountDetails3
from ._LoyaltyProgramme4 import LoyaltyProgramme4
from ._HiredVehicle3 import HiredVehicle3
from ._TrueFalseIndicator import TrueFalseIndicator
from ._AdditionalData1 import AdditionalData1
from ._Max35Text import Max35Text
from ._AncillaryPurchase3 import AncillaryPurchase3

class PassengerTransport3(base_types._BaseFieldType):

	__slots__ = ["_OrgnlRsvatnSys", "_LltyPrgrmm", "_CstmrRef", "_TripLeg", "_Insrnc", "_DocNb", "_Drtn", "_Pssngr", "_RsvatnNb", "_TtlAmt", "_Dprture", "_TrvlAuthstnCd", "_RsvatnSys", "_AddtlData", "_SummryCmmdtyId", "_HirdVhclDtls", "_OrgnlRsvatnNb", "_TcktIssr", "_OpnTckt", "_AncllryPurchs"]
	@property
	def OrgnlRsvatnSys(self):
		return self._OrgnlRsvatnSys

	@OrgnlRsvatnSys.setter
	def OrgnlRsvatnSys(self, value):
		self._OrgnlRsvatnSys = value if type(value) != base_types.auto else self.make_default("OrgnlRsvatnSys")

	@OrgnlRsvatnSys.deleter
	def OrgnlRsvatnSys(self):
		del self._OrgnlRsvatnSys
		self._OrgnlRsvatnSys = None

	@property
	def LltyPrgrmm(self):
		return self._LltyPrgrmm

	@LltyPrgrmm.setter
	def LltyPrgrmm(self, value):
		self._LltyPrgrmm = value if type(value) != base_types.auto else self.make_default("LltyPrgrmm")

	@LltyPrgrmm.deleter
	def LltyPrgrmm(self):
		del self._LltyPrgrmm
		self._LltyPrgrmm = None

	@property
	def CstmrRef(self):
		return self._CstmrRef

	@CstmrRef.setter
	def CstmrRef(self, value):
		self._CstmrRef = value if type(value) != base_types.auto else self.make_default("CstmrRef")

	@CstmrRef.deleter
	def CstmrRef(self):
		del self._CstmrRef
		self._CstmrRef = None

	@property
	def TripLeg(self):
		return self._TripLeg

	@TripLeg.setter
	def TripLeg(self, value):
		self._TripLeg = value if type(value) != base_types.auto else self.make_default("TripLeg")

	@TripLeg.deleter
	def TripLeg(self):
		del self._TripLeg
		self._TripLeg = None

	@property
	def Insrnc(self):
		return self._Insrnc

	@Insrnc.setter
	def Insrnc(self, value):
		self._Insrnc = value if type(value) != base_types.auto else self.make_default("Insrnc")

	@Insrnc.deleter
	def Insrnc(self):
		del self._Insrnc
		self._Insrnc = None

	@property
	def DocNb(self):
		return self._DocNb

	@DocNb.setter
	def DocNb(self, value):
		self._DocNb = value if type(value) != base_types.auto else self.make_default("DocNb")

	@DocNb.deleter
	def DocNb(self):
		del self._DocNb
		self._DocNb = None

	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if type(value) != base_types.auto else self.make_default("Drtn")

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = None

	@property
	def Pssngr(self):
		return self._Pssngr

	@Pssngr.setter
	def Pssngr(self, value):
		self._Pssngr = value if type(value) != base_types.auto else self.make_default("Pssngr")

	@Pssngr.deleter
	def Pssngr(self):
		del self._Pssngr
		self._Pssngr = None

	@property
	def RsvatnNb(self):
		return self._RsvatnNb

	@RsvatnNb.setter
	def RsvatnNb(self, value):
		self._RsvatnNb = value if type(value) != base_types.auto else self.make_default("RsvatnNb")

	@RsvatnNb.deleter
	def RsvatnNb(self):
		del self._RsvatnNb
		self._RsvatnNb = None

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if type(value) != base_types.auto else self.make_default("TtlAmt")

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = None

	@property
	def Dprture(self):
		return self._Dprture

	@Dprture.setter
	def Dprture(self, value):
		self._Dprture = value if type(value) != base_types.auto else self.make_default("Dprture")

	@Dprture.deleter
	def Dprture(self):
		del self._Dprture
		self._Dprture = None

	@property
	def TrvlAuthstnCd(self):
		return self._TrvlAuthstnCd

	@TrvlAuthstnCd.setter
	def TrvlAuthstnCd(self, value):
		self._TrvlAuthstnCd = value if type(value) != base_types.auto else self.make_default("TrvlAuthstnCd")

	@TrvlAuthstnCd.deleter
	def TrvlAuthstnCd(self):
		del self._TrvlAuthstnCd
		self._TrvlAuthstnCd = None

	@property
	def RsvatnSys(self):
		return self._RsvatnSys

	@RsvatnSys.setter
	def RsvatnSys(self, value):
		self._RsvatnSys = value if type(value) != base_types.auto else self.make_default("RsvatnSys")

	@RsvatnSys.deleter
	def RsvatnSys(self):
		del self._RsvatnSys
		self._RsvatnSys = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != base_types.auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def SummryCmmdtyId(self):
		return self._SummryCmmdtyId

	@SummryCmmdtyId.setter
	def SummryCmmdtyId(self, value):
		self._SummryCmmdtyId = value if type(value) != base_types.auto else self.make_default("SummryCmmdtyId")

	@SummryCmmdtyId.deleter
	def SummryCmmdtyId(self):
		del self._SummryCmmdtyId
		self._SummryCmmdtyId = None

	@property
	def HirdVhclDtls(self):
		return self._HirdVhclDtls

	@HirdVhclDtls.setter
	def HirdVhclDtls(self, value):
		self._HirdVhclDtls = value if type(value) != base_types.auto else self.make_default("HirdVhclDtls")

	@HirdVhclDtls.deleter
	def HirdVhclDtls(self):
		del self._HirdVhclDtls
		self._HirdVhclDtls = None

	@property
	def OrgnlRsvatnNb(self):
		return self._OrgnlRsvatnNb

	@OrgnlRsvatnNb.setter
	def OrgnlRsvatnNb(self, value):
		self._OrgnlRsvatnNb = value if type(value) != base_types.auto else self.make_default("OrgnlRsvatnNb")

	@OrgnlRsvatnNb.deleter
	def OrgnlRsvatnNb(self):
		del self._OrgnlRsvatnNb
		self._OrgnlRsvatnNb = None

	@property
	def TcktIssr(self):
		return self._TcktIssr

	@TcktIssr.setter
	def TcktIssr(self, value):
		self._TcktIssr = value if type(value) != base_types.auto else self.make_default("TcktIssr")

	@TcktIssr.deleter
	def TcktIssr(self):
		del self._TcktIssr
		self._TcktIssr = None

	@property
	def OpnTckt(self):
		return self._OpnTckt

	@OpnTckt.setter
	def OpnTckt(self, value):
		self._OpnTckt = value if type(value) != base_types.auto else self.make_default("OpnTckt")

	@OpnTckt.deleter
	def OpnTckt(self):
		del self._OpnTckt
		self._OpnTckt = None

	@property
	def AncllryPurchs(self):
		return self._AncllryPurchs

	@AncllryPurchs.setter
	def AncllryPurchs(self, value):
		self._AncllryPurchs = value if type(value) != base_types.auto else self.make_default("AncllryPurchs")

	@AncllryPurchs.deleter
	def AncllryPurchs(self):
		del self._AncllryPurchs
		self._AncllryPurchs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlRsvatnSys', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyPrgrmm', type=LoyaltyProgramme4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrRef', type=CustomerReference1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TripLeg', type=TripLeg3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Insrnc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drtn', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pssngr', type=Customer9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RsvatnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=AmountDetails3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dprture', type=DepartureOrArrival1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrvlAuthstnCd', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsvatnSys', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HirdVhclDtls', type=HiredVehicle3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlRsvatnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TcktIssr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpnTckt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AncllryPurchs', type=AncillaryPurchase3, min=0, max=None, mutex_group=None, array=True),
	))

