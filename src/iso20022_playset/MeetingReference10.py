import base_types
import Max35Text
import PostalAddress1
import MeetingTypeClassification2Choice
import PartyIdentification129Choice
import MeetingType4Code
import ISODateTime

class MeetingReference10(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_MtgId", "_Issr", "_Clssfctn", "_Lctn", "_MtgDtAndTm", "_IssrMtgId"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def MtgId(self):
		return self._MtgId

	@MtgId.setter
	def MtgId(self, value):
		self._MtgId = value if type(value) != auto else self.make_default("MtgId")

	@MtgId.deleter
	def MtgId(self):
		del self._MtgId
		self._MtgId = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	@property
	def Clssfctn(self):
		return self._Clssfctn

	@Clssfctn.setter
	def Clssfctn(self, value):
		self._Clssfctn = value if type(value) != auto else self.make_default("Clssfctn")

	@Clssfctn.deleter
	def Clssfctn(self):
		del self._Clssfctn
		self._Clssfctn = None

	@property
	def Lctn(self):
		return self._Lctn

	@Lctn.setter
	def Lctn(self, value):
		self._Lctn = value if type(value) != auto else self.make_default("Lctn")

	@Lctn.deleter
	def Lctn(self):
		del self._Lctn
		self._Lctn = None

	@property
	def MtgDtAndTm(self):
		return self._MtgDtAndTm

	@MtgDtAndTm.setter
	def MtgDtAndTm(self, value):
		self._MtgDtAndTm = value if type(value) != auto else self.make_default("MtgDtAndTm")

	@MtgDtAndTm.deleter
	def MtgDtAndTm(self):
		del self._MtgDtAndTm
		self._MtgDtAndTm = None

	@property
	def IssrMtgId(self):
		return self._IssrMtgId

	@IssrMtgId.setter
	def IssrMtgId(self, value):
		self._IssrMtgId = value if type(value) != auto else self.make_default("IssrMtgId")

	@IssrMtgId.deleter
	def IssrMtgId(self):
		del self._IssrMtgId
		self._IssrMtgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=MeetingType4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification129Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Clssfctn', type=MeetingTypeClassification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lctn', type=PostalAddress1, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='MtgDtAndTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrMtgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

