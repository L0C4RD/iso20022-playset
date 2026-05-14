# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PartyIdentification239Choice import PartyIdentification239Choice
from ._PartyIdentificationAndAccount200 import PartyIdentificationAndAccount200
from ._PartyIdentificationAndAccount201 import PartyIdentificationAndAccount201

class ReceivingPartiesAndAccount19(base_types._BaseFieldType):

	__slots__ = ["_Dpstry", "_Pty1", "_Pty2"]
	@property
	def Dpstry(self):
		return self._Dpstry

	@Dpstry.setter
	def Dpstry(self, value):
		self._Dpstry = value if type(value) != base_types.auto else self.make_default("Dpstry")

	@Dpstry.deleter
	def Dpstry(self):
		del self._Dpstry
		self._Dpstry = None

	@property
	def Pty1(self):
		return self._Pty1

	@Pty1.setter
	def Pty1(self, value):
		self._Pty1 = value if type(value) != base_types.auto else self.make_default("Pty1")

	@Pty1.deleter
	def Pty1(self):
		del self._Pty1
		self._Pty1 = None

	@property
	def Pty2(self):
		return self._Pty2

	@Pty2.setter
	def Pty2(self, value):
		self._Pty2 = value if type(value) != base_types.auto else self.make_default("Pty2")

	@Pty2.deleter
	def Pty2(self):
		del self._Pty2
		self._Pty2 = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dpstry', type=PartyIdentification239Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty1', type=PartyIdentificationAndAccount200, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty2', type=PartyIdentificationAndAccount201, min=0, max=1, mutex_group=None, array=False),
	))