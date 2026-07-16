# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import Address4
from . import ContactBusiness2
from . import Max35Text
from . import Max70Text
from . import TravelAgencyPackage2

class TravelAgency5(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_Assgnr", "_Cd", "_Ctct", "_IATACd", "_Nm", "_NtlData", "_PrvtData", "_ShrtNm", "_TrvlPackg"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', Address4, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', Address4, False)

	@property
	def Assgnr(self):
		return self._Assgnr

	@Assgnr.setter
	def Assgnr(self, value):
		self._Assgnr = value if value is not None else base_types.UninitialisedField(self, 'Assgnr', Max35Text, False)

	@Assgnr.deleter
	def Assgnr(self):
		del self._Assgnr
		self._Assgnr = base_types.UninitialisedField(self, 'Assgnr', Max35Text, False)

	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', Max35Text, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', Max35Text, False)

	@property
	def Ctct(self):
		return self._Ctct

	@Ctct.setter
	def Ctct(self, value):
		self._Ctct = value if value is not None else base_types.UninitialisedField(self, 'Ctct', ContactBusiness2, False)

	@Ctct.deleter
	def Ctct(self):
		del self._Ctct
		self._Ctct = base_types.UninitialisedField(self, 'Ctct', ContactBusiness2, False)

	@property
	def IATACd(self):
		return self._IATACd

	@IATACd.setter
	def IATACd(self, value):
		self._IATACd = value if value is not None else base_types.UninitialisedField(self, 'IATACd', Max35Text, False)

	@IATACd.deleter
	def IATACd(self):
		del self._IATACd
		self._IATACd = base_types.UninitialisedField(self, 'IATACd', Max35Text, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max70Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max70Text, False)

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

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
	def TrvlPackg(self):
		return self._TrvlPackg

	@TrvlPackg.setter
	def TrvlPackg(self, value):
		self._TrvlPackg = value if value is not None else base_types.UninitialisedField(self, 'TrvlPackg', TravelAgencyPackage2, True)

	@TrvlPackg.deleter
	def TrvlPackg(self):
		del self._TrvlPackg
		self._TrvlPackg = base_types.UninitialisedField(self, 'TrvlPackg', TravelAgencyPackage2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=Address4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assgnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctct', type=ContactBusiness2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IATACd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrvlPackg', type=TravelAgencyPackage2, min=0, max=None, mutex_group=None, array=True),
	))