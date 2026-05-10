import base_types
import PartyIdentificationAndAccount163
import PartyIdentification316

class SettlementParties123(base_types._BaseFieldType):

	__slots__ = ["_Pty1", "_Dpstry", "_Pty2", "_Pty3"]
	@property
	def Pty1(self):
		return self._Pty1

	@Pty1.setter
	def Pty1(self, value):
		self._Pty1 = value if type(value) != auto else self.make_default("Pty1")

	@Pty1.deleter
	def Pty1(self):
		del self._Pty1
		self._Pty1 = None

	@property
	def Dpstry(self):
		return self._Dpstry

	@Dpstry.setter
	def Dpstry(self, value):
		self._Dpstry = value if type(value) != auto else self.make_default("Dpstry")

	@Dpstry.deleter
	def Dpstry(self):
		del self._Dpstry
		self._Dpstry = None

	@property
	def Pty2(self):
		return self._Pty2

	@Pty2.setter
	def Pty2(self, value):
		self._Pty2 = value if type(value) != auto else self.make_default("Pty2")

	@Pty2.deleter
	def Pty2(self):
		del self._Pty2
		self._Pty2 = None

	@property
	def Pty3(self):
		return self._Pty3

	@Pty3.setter
	def Pty3(self, value):
		self._Pty3 = value if type(value) != auto else self.make_default("Pty3")

	@Pty3.deleter
	def Pty3(self):
		del self._Pty3
		self._Pty3 = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pty1', type=PartyIdentificationAndAccount163, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dpstry', type=PartyIdentification316, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty2', type=PartyIdentificationAndAccount163, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty3', type=PartyIdentificationAndAccount163, min=0, max=1, mutex_group=None, array=False),
	))

