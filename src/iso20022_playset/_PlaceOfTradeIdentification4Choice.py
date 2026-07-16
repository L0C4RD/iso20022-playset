# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AnyBICDec2014Identifier
from . import CountryCode
from . import MICIdentifier
from . import Max35Text

class PlaceOfTradeIdentification4Choice(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_OverTheCntr", "_Pty", "_Xchg"]
	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@property
	def OverTheCntr(self):
		return self._OverTheCntr

	@OverTheCntr.setter
	def OverTheCntr(self, value):
		self._OverTheCntr = value if value is not None else base_types.UninitialisedField(self, 'OverTheCntr', Max35Text, False)

	@OverTheCntr.deleter
	def OverTheCntr(self):
		del self._OverTheCntr
		self._OverTheCntr = base_types.UninitialisedField(self, 'OverTheCntr', Max35Text, False)

	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if value is not None else base_types.UninitialisedField(self, 'Pty', AnyBICDec2014Identifier, False)

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = base_types.UninitialisedField(self, 'Pty', AnyBICDec2014Identifier, False)

	@property
	def Xchg(self):
		return self._Xchg

	@Xchg.setter
	def Xchg(self, value):
		self._Xchg = value if value is not None else base_types.UninitialisedField(self, 'Xchg', MICIdentifier, False)

	@Xchg.deleter
	def Xchg(self):
		del self._Xchg
		self._Xchg = base_types.UninitialisedField(self, 'Xchg', MICIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OverTheCntr', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pty', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Xchg', type=MICIdentifier, min=0, max=1, mutex_group=1, array=False),
	))