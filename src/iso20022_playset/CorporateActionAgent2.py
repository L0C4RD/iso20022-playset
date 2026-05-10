import base_types
import PartyIdentification289

class CorporateActionAgent2(base_types._BaseFieldType):

	__slots__ = ["_SlctnAgt", "_IssrAgt", "_PngAgt", "_RedAgt", "_Issr", "_RmktgAgt", "_InfAgt", "_TrfAgt", "_Regar"]
	@property
	def SlctnAgt(self):
		return self._SlctnAgt

	@SlctnAgt.setter
	def SlctnAgt(self, value):
		self._SlctnAgt = value if type(value) != auto else self.make_default("SlctnAgt")

	@SlctnAgt.deleter
	def SlctnAgt(self):
		del self._SlctnAgt
		self._SlctnAgt = None

	@property
	def IssrAgt(self):
		return self._IssrAgt

	@IssrAgt.setter
	def IssrAgt(self, value):
		self._IssrAgt = value if type(value) != auto else self.make_default("IssrAgt")

	@IssrAgt.deleter
	def IssrAgt(self):
		del self._IssrAgt
		self._IssrAgt = None

	@property
	def PngAgt(self):
		return self._PngAgt

	@PngAgt.setter
	def PngAgt(self, value):
		self._PngAgt = value if type(value) != auto else self.make_default("PngAgt")

	@PngAgt.deleter
	def PngAgt(self):
		del self._PngAgt
		self._PngAgt = None

	@property
	def RedAgt(self):
		return self._RedAgt

	@RedAgt.setter
	def RedAgt(self, value):
		self._RedAgt = value if type(value) != auto else self.make_default("RedAgt")

	@RedAgt.deleter
	def RedAgt(self):
		del self._RedAgt
		self._RedAgt = None

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
	def RmktgAgt(self):
		return self._RmktgAgt

	@RmktgAgt.setter
	def RmktgAgt(self, value):
		self._RmktgAgt = value if type(value) != auto else self.make_default("RmktgAgt")

	@RmktgAgt.deleter
	def RmktgAgt(self):
		del self._RmktgAgt
		self._RmktgAgt = None

	@property
	def InfAgt(self):
		return self._InfAgt

	@InfAgt.setter
	def InfAgt(self, value):
		self._InfAgt = value if type(value) != auto else self.make_default("InfAgt")

	@InfAgt.deleter
	def InfAgt(self):
		del self._InfAgt
		self._InfAgt = None

	@property
	def TrfAgt(self):
		return self._TrfAgt

	@TrfAgt.setter
	def TrfAgt(self, value):
		self._TrfAgt = value if type(value) != auto else self.make_default("TrfAgt")

	@TrfAgt.deleter
	def TrfAgt(self):
		del self._TrfAgt
		self._TrfAgt = None

	@property
	def Regar(self):
		return self._Regar

	@Regar.setter
	def Regar(self, value):
		self._Regar = value if type(value) != auto else self.make_default("Regar")

	@Regar.deleter
	def Regar(self):
		del self._Regar
		self._Regar = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SlctnAgt', type=PartyIdentification289, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrAgt', type=PartyIdentification289, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PngAgt', type=PartyIdentification289, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedAgt', type=PartyIdentification289, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification289, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmktgAgt', type=PartyIdentification289, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfAgt', type=PartyIdentification289, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfAgt', type=PartyIdentification289, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Regar', type=PartyIdentification289, min=0, max=1, mutex_group=None, array=False),
	))

