# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyCancellation1
from . import PartyUpdate1

class PartyReport1Choice(base_types._BaseFieldType):

	__slots__ = ["_Cxl", "_Upd"]
	@property
	def Cxl(self):
		return self._Cxl

	@Cxl.setter
	def Cxl(self, value):
		self._Cxl = value if value is not None else base_types.UninitialisedField(self, 'Cxl', PartyCancellation1, False)

	@Cxl.deleter
	def Cxl(self):
		del self._Cxl
		self._Cxl = base_types.UninitialisedField(self, 'Cxl', PartyCancellation1, False)

	@property
	def Upd(self):
		return self._Upd

	@Upd.setter
	def Upd(self, value):
		self._Upd = value if value is not None else base_types.UninitialisedField(self, 'Upd', PartyUpdate1, False)

	@Upd.deleter
	def Upd(self):
		del self._Upd
		self._Upd = base_types.UninitialisedField(self, 'Upd', PartyUpdate1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cxl', type=PartyCancellation1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Upd', type=PartyUpdate1, min=0, max=1, mutex_group=1, array=False),
	))