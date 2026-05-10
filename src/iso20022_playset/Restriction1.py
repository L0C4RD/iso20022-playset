import base_types
import ISODateTime
import CodeOrProprietary1Choice

class Restriction1(base_types._BaseFieldType):

	__slots__ = ["_VldFr", "_VldUntil", "_RstrctnTp"]
	@property
	def VldFr(self):
		return self._VldFr

	@VldFr.setter
	def VldFr(self, value):
		self._VldFr = value if type(value) != auto else self.make_default("VldFr")

	@VldFr.deleter
	def VldFr(self):
		del self._VldFr
		self._VldFr = None

	@property
	def VldUntil(self):
		return self._VldUntil

	@VldUntil.setter
	def VldUntil(self, value):
		self._VldUntil = value if type(value) != auto else self.make_default("VldUntil")

	@VldUntil.deleter
	def VldUntil(self):
		del self._VldUntil
		self._VldUntil = None

	@property
	def RstrctnTp(self):
		return self._RstrctnTp

	@RstrctnTp.setter
	def RstrctnTp(self, value):
		self._RstrctnTp = value if type(value) != auto else self.make_default("RstrctnTp")

	@RstrctnTp.deleter
	def RstrctnTp(self):
		del self._RstrctnTp
		self._RstrctnTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VldFr', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldUntil', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctnTp', type=CodeOrProprietary1Choice, min=1, max=1, mutex_group=None, array=False),
	))

