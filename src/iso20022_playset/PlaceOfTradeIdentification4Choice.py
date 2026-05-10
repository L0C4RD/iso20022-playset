from . import base_types
import CountryCode
import MICIdentifier
import AnyBICDec2014Identifier
import Max35Text

class PlaceOfTradeIdentification4Choice(base_types._BaseFieldType):

	__slots__ = ["_Xchg", "_OverTheCntr", "_Pty", "_Ctry"]
	@property
	def Xchg(self):
		return self._Xchg

	@Xchg.setter
	def Xchg(self, value):
		self._Xchg = value if type(value) != auto else self.make_default("Xchg")

	@Xchg.deleter
	def Xchg(self):
		del self._Xchg
		self._Xchg = None

	@property
	def OverTheCntr(self):
		return self._OverTheCntr

	@OverTheCntr.setter
	def OverTheCntr(self, value):
		self._OverTheCntr = value if type(value) != auto else self.make_default("OverTheCntr")

	@OverTheCntr.deleter
	def OverTheCntr(self):
		del self._OverTheCntr
		self._OverTheCntr = None

	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if type(value) != auto else self.make_default("Pty")

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Xchg', type=MICIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OverTheCntr', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pty', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
	))

