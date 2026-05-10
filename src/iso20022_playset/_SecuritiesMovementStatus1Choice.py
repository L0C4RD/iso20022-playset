from . import base_types
from ._ProprietaryReason4 import ProprietaryReason4

class SecuritiesMovementStatus1Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Ccy", "_Csh", "_Elgblty", "_Excld", "_Futr", "_MnlyAccptd", "_Pdg", "_Tax", "_Wait"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def Csh(self):
		return self._Csh

	@Csh.setter
	def Csh(self, value):
		self._Csh = value if type(value) != base_types.auto else self.make_default("Csh")

	@Csh.deleter
	def Csh(self):
		del self._Csh
		self._Csh = None

	@property
	def Elgblty(self):
		return self._Elgblty

	@Elgblty.setter
	def Elgblty(self, value):
		self._Elgblty = value if type(value) != base_types.auto else self.make_default("Elgblty")

	@Elgblty.deleter
	def Elgblty(self):
		del self._Elgblty
		self._Elgblty = None

	@property
	def Excld(self):
		return self._Excld

	@Excld.setter
	def Excld(self, value):
		self._Excld = value if type(value) != base_types.auto else self.make_default("Excld")

	@Excld.deleter
	def Excld(self):
		del self._Excld
		self._Excld = None

	@property
	def Futr(self):
		return self._Futr

	@Futr.setter
	def Futr(self, value):
		self._Futr = value if type(value) != base_types.auto else self.make_default("Futr")

	@Futr.deleter
	def Futr(self):
		del self._Futr
		self._Futr = None

	@property
	def MnlyAccptd(self):
		return self._MnlyAccptd

	@MnlyAccptd.setter
	def MnlyAccptd(self, value):
		self._MnlyAccptd = value if type(value) != base_types.auto else self.make_default("MnlyAccptd")

	@MnlyAccptd.deleter
	def MnlyAccptd(self):
		del self._MnlyAccptd
		self._MnlyAccptd = None

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if type(value) != base_types.auto else self.make_default("Pdg")

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = None

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != base_types.auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	@property
	def Wait(self):
		return self._Wait

	@Wait.setter
	def Wait(self, value):
		self._Wait = value if type(value) != base_types.auto else self.make_default("Wait")

	@Wait.deleter
	def Wait(self):
		del self._Wait
		self._Wait = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ccy', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Csh', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Elgblty', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Excld', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Futr', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MnlyAccptd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Tax', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Wait', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
	))

