import base_types
import PositionSet17
import PositionSet18
import PositionSet16
import PositionSet19
import PositionSet20
import ISODate

class NamedPosition3(base_types._BaseFieldType):

	__slots__ = ["_Ln", "_RefDt", "_Reuse", "_Mrgn", "_GnlInf", "_Coll"]
	@property
	def Ln(self):
		return self._Ln

	@Ln.setter
	def Ln(self, value):
		self._Ln = value if type(value) != auto else self.make_default("Ln")

	@Ln.deleter
	def Ln(self):
		del self._Ln
		self._Ln = None

	@property
	def RefDt(self):
		return self._RefDt

	@RefDt.setter
	def RefDt(self, value):
		self._RefDt = value if type(value) != auto else self.make_default("RefDt")

	@RefDt.deleter
	def RefDt(self):
		del self._RefDt
		self._RefDt = None

	@property
	def Reuse(self):
		return self._Reuse

	@Reuse.setter
	def Reuse(self, value):
		self._Reuse = value if type(value) != auto else self.make_default("Reuse")

	@Reuse.deleter
	def Reuse(self):
		del self._Reuse
		self._Reuse = None

	@property
	def Mrgn(self):
		return self._Mrgn

	@Mrgn.setter
	def Mrgn(self, value):
		self._Mrgn = value if type(value) != auto else self.make_default("Mrgn")

	@Mrgn.deleter
	def Mrgn(self):
		del self._Mrgn
		self._Mrgn = None

	@property
	def GnlInf(self):
		return self._GnlInf

	@GnlInf.setter
	def GnlInf(self, value):
		self._GnlInf = value if type(value) != auto else self.make_default("GnlInf")

	@GnlInf.deleter
	def GnlInf(self):
		del self._GnlInf
		self._GnlInf = None

	@property
	def Coll(self):
		return self._Coll

	@Coll.setter
	def Coll(self, value):
		self._Coll = value if type(value) != auto else self.make_default("Coll")

	@Coll.deleter
	def Coll(self):
		del self._Coll
		self._Coll = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ln', type=PositionSet17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RefDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Reuse', type=PositionSet19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Mrgn', type=PositionSet20, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GnlInf', type=PositionSet16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Coll', type=PositionSet18, min=0, max=None, mutex_group=None, array=True),
	))

