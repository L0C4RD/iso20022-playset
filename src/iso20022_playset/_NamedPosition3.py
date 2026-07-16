# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import PositionSet16
from . import PositionSet17
from . import PositionSet18
from . import PositionSet19
from . import PositionSet20

class NamedPosition3(base_types._BaseFieldType):

	__slots__ = ["_Coll", "_GnlInf", "_Ln", "_Mrgn", "_RefDt", "_Reuse"]
	@property
	def Coll(self):
		return self._Coll

	@Coll.setter
	def Coll(self, value):
		self._Coll = value if value is not None else base_types.UninitialisedField(self, 'Coll', PositionSet18, True)

	@Coll.deleter
	def Coll(self):
		del self._Coll
		self._Coll = base_types.UninitialisedField(self, 'Coll', PositionSet18, True)

	@property
	def GnlInf(self):
		return self._GnlInf

	@GnlInf.setter
	def GnlInf(self, value):
		self._GnlInf = value if value is not None else base_types.UninitialisedField(self, 'GnlInf', PositionSet16, True)

	@GnlInf.deleter
	def GnlInf(self):
		del self._GnlInf
		self._GnlInf = base_types.UninitialisedField(self, 'GnlInf', PositionSet16, True)

	@property
	def Ln(self):
		return self._Ln

	@Ln.setter
	def Ln(self, value):
		self._Ln = value if value is not None else base_types.UninitialisedField(self, 'Ln', PositionSet17, True)

	@Ln.deleter
	def Ln(self):
		del self._Ln
		self._Ln = base_types.UninitialisedField(self, 'Ln', PositionSet17, True)

	@property
	def Mrgn(self):
		return self._Mrgn

	@Mrgn.setter
	def Mrgn(self, value):
		self._Mrgn = value if value is not None else base_types.UninitialisedField(self, 'Mrgn', PositionSet20, True)

	@Mrgn.deleter
	def Mrgn(self):
		del self._Mrgn
		self._Mrgn = base_types.UninitialisedField(self, 'Mrgn', PositionSet20, True)

	@property
	def RefDt(self):
		return self._RefDt

	@RefDt.setter
	def RefDt(self, value):
		self._RefDt = value if value is not None else base_types.UninitialisedField(self, 'RefDt', ISODate, False)

	@RefDt.deleter
	def RefDt(self):
		del self._RefDt
		self._RefDt = base_types.UninitialisedField(self, 'RefDt', ISODate, False)

	@property
	def Reuse(self):
		return self._Reuse

	@Reuse.setter
	def Reuse(self, value):
		self._Reuse = value if value is not None else base_types.UninitialisedField(self, 'Reuse', PositionSet19, True)

	@Reuse.deleter
	def Reuse(self):
		del self._Reuse
		self._Reuse = base_types.UninitialisedField(self, 'Reuse', PositionSet19, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Coll', type=PositionSet18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GnlInf', type=PositionSet16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ln', type=PositionSet17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Mrgn', type=PositionSet20, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RefDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Reuse', type=PositionSet19, min=0, max=None, mutex_group=None, array=True),
	))