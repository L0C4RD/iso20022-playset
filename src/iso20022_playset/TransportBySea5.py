import base_types
import Max35Text
import Exact7NumericText
import CountryCode
import Max70Text

class TransportBySea5(base_types._BaseFieldType):

	__slots__ = ["_PortOfLoadng", "_VsslNm", "_MstrNm", "_OwnrNm", "_IMONb", "_CrrierAgtNm", "_VygNb", "_PortOfDschrge", "_SeaCrrierNm", "_ChrtrrNm", "_CrrierAgtCtry", "_SeaCrrierCtry"]
	@property
	def PortOfLoadng(self):
		return self._PortOfLoadng

	@PortOfLoadng.setter
	def PortOfLoadng(self, value):
		self._PortOfLoadng = value if type(value) != auto else self.make_default("PortOfLoadng")

	@PortOfLoadng.deleter
	def PortOfLoadng(self):
		del self._PortOfLoadng
		self._PortOfLoadng = None

	@property
	def VsslNm(self):
		return self._VsslNm

	@VsslNm.setter
	def VsslNm(self, value):
		self._VsslNm = value if type(value) != auto else self.make_default("VsslNm")

	@VsslNm.deleter
	def VsslNm(self):
		del self._VsslNm
		self._VsslNm = None

	@property
	def MstrNm(self):
		return self._MstrNm

	@MstrNm.setter
	def MstrNm(self, value):
		self._MstrNm = value if type(value) != auto else self.make_default("MstrNm")

	@MstrNm.deleter
	def MstrNm(self):
		del self._MstrNm
		self._MstrNm = None

	@property
	def OwnrNm(self):
		return self._OwnrNm

	@OwnrNm.setter
	def OwnrNm(self, value):
		self._OwnrNm = value if type(value) != auto else self.make_default("OwnrNm")

	@OwnrNm.deleter
	def OwnrNm(self):
		del self._OwnrNm
		self._OwnrNm = None

	@property
	def IMONb(self):
		return self._IMONb

	@IMONb.setter
	def IMONb(self, value):
		self._IMONb = value if type(value) != auto else self.make_default("IMONb")

	@IMONb.deleter
	def IMONb(self):
		del self._IMONb
		self._IMONb = None

	@property
	def CrrierAgtNm(self):
		return self._CrrierAgtNm

	@CrrierAgtNm.setter
	def CrrierAgtNm(self, value):
		self._CrrierAgtNm = value if type(value) != auto else self.make_default("CrrierAgtNm")

	@CrrierAgtNm.deleter
	def CrrierAgtNm(self):
		del self._CrrierAgtNm
		self._CrrierAgtNm = None

	@property
	def VygNb(self):
		return self._VygNb

	@VygNb.setter
	def VygNb(self, value):
		self._VygNb = value if type(value) != auto else self.make_default("VygNb")

	@VygNb.deleter
	def VygNb(self):
		del self._VygNb
		self._VygNb = None

	@property
	def PortOfDschrge(self):
		return self._PortOfDschrge

	@PortOfDschrge.setter
	def PortOfDschrge(self, value):
		self._PortOfDschrge = value if type(value) != auto else self.make_default("PortOfDschrge")

	@PortOfDschrge.deleter
	def PortOfDschrge(self):
		del self._PortOfDschrge
		self._PortOfDschrge = None

	@property
	def SeaCrrierNm(self):
		return self._SeaCrrierNm

	@SeaCrrierNm.setter
	def SeaCrrierNm(self, value):
		self._SeaCrrierNm = value if type(value) != auto else self.make_default("SeaCrrierNm")

	@SeaCrrierNm.deleter
	def SeaCrrierNm(self):
		del self._SeaCrrierNm
		self._SeaCrrierNm = None

	@property
	def ChrtrrNm(self):
		return self._ChrtrrNm

	@ChrtrrNm.setter
	def ChrtrrNm(self, value):
		self._ChrtrrNm = value if type(value) != auto else self.make_default("ChrtrrNm")

	@ChrtrrNm.deleter
	def ChrtrrNm(self):
		del self._ChrtrrNm
		self._ChrtrrNm = None

	@property
	def CrrierAgtCtry(self):
		return self._CrrierAgtCtry

	@CrrierAgtCtry.setter
	def CrrierAgtCtry(self, value):
		self._CrrierAgtCtry = value if type(value) != auto else self.make_default("CrrierAgtCtry")

	@CrrierAgtCtry.deleter
	def CrrierAgtCtry(self):
		del self._CrrierAgtCtry
		self._CrrierAgtCtry = None

	@property
	def SeaCrrierCtry(self):
		return self._SeaCrrierCtry

	@SeaCrrierCtry.setter
	def SeaCrrierCtry(self, value):
		self._SeaCrrierCtry = value if type(value) != auto else self.make_default("SeaCrrierCtry")

	@SeaCrrierCtry.deleter
	def SeaCrrierCtry(self):
		del self._SeaCrrierCtry
		self._SeaCrrierCtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PortOfLoadng', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VsslNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IMONb', type=Exact7NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrierAgtNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VygNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PortOfDschrge', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeaCrrierNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrtrrNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrierAgtCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeaCrrierCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
	))

