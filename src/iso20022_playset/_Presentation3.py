# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Channel1Choice
from . import DocumentFormat1Choice
from . import Max256Text

class Presentation3(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_Chanl", "_Frmt"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', Max256Text, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', Max256Text, False)

	@property
	def Chanl(self):
		return self._Chanl

	@Chanl.setter
	def Chanl(self, value):
		self._Chanl = value if value is not None else base_types.UninitialisedField(self, 'Chanl', Channel1Choice, False)

	@Chanl.deleter
	def Chanl(self):
		del self._Chanl
		self._Chanl = base_types.UninitialisedField(self, 'Chanl', Channel1Choice, False)

	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if value is not None else base_types.UninitialisedField(self, 'Frmt', DocumentFormat1Choice, False)

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = base_types.UninitialisedField(self, 'Frmt', DocumentFormat1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chanl', type=Channel1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frmt', type=DocumentFormat1Choice, min=0, max=1, mutex_group=None, array=False),
	))