from . import base_types
import Address2
import ContactBusiness1
import AdditionalData1
import Max70Text
import Max35Text
import TravelAgencyPackage2

class TravelAgency4(base_types._BaseFieldType):

	__slots__ = ["_IATACd", "_Adr", "_Assgnr", "_Ctct", "_AddtlData", "_TrvlPackg", "_ShrtNm", "_Nm", "_Cd"]
	@property
	def IATACd(self):
		return self._IATACd

	@IATACd.setter
	def IATACd(self, value):
		self._IATACd = value if type(value) != auto else self.make_default("IATACd")

	@IATACd.deleter
	def IATACd(self):
		del self._IATACd
		self._IATACd = None

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

	@property
	def Assgnr(self):
		return self._Assgnr

	@Assgnr.setter
	def Assgnr(self, value):
		self._Assgnr = value if type(value) != auto else self.make_default("Assgnr")

	@Assgnr.deleter
	def Assgnr(self):
		del self._Assgnr
		self._Assgnr = None

	@property
	def Ctct(self):
		return self._Ctct

	@Ctct.setter
	def Ctct(self, value):
		self._Ctct = value if type(value) != auto else self.make_default("Ctct")

	@Ctct.deleter
	def Ctct(self):
		del self._Ctct
		self._Ctct = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def TrvlPackg(self):
		return self._TrvlPackg

	@TrvlPackg.setter
	def TrvlPackg(self, value):
		self._TrvlPackg = value if type(value) != auto else self.make_default("TrvlPackg")

	@TrvlPackg.deleter
	def TrvlPackg(self):
		del self._TrvlPackg
		self._TrvlPackg = None

	@property
	def ShrtNm(self):
		return self._ShrtNm

	@ShrtNm.setter
	def ShrtNm(self, value):
		self._ShrtNm = value if type(value) != auto else self.make_default("ShrtNm")

	@ShrtNm.deleter
	def ShrtNm(self):
		del self._ShrtNm
		self._ShrtNm = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IATACd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assgnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctct', type=ContactBusiness1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrvlPackg', type=TravelAgencyPackage2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

