# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CodeOrProprietary1Choice import CodeOrProprietary1Choice
from ._ISODateTime import ISODateTime

class Restriction1(base_types._BaseFieldType):

	__slots__ = ["_RstrctnTp", "_VldFr", "_VldUntil"]
	@property
	def RstrctnTp(self):
		return self._RstrctnTp

	@RstrctnTp.setter
	def RstrctnTp(self, value):
		self._RstrctnTp = value if type(value) != base_types.auto else self.make_default("RstrctnTp")

	@RstrctnTp.deleter
	def RstrctnTp(self):
		del self._RstrctnTp
		self._RstrctnTp = None

	@property
	def VldFr(self):
		return self._VldFr

	@VldFr.setter
	def VldFr(self, value):
		self._VldFr = value if type(value) != base_types.auto else self.make_default("VldFr")

	@VldFr.deleter
	def VldFr(self):
		del self._VldFr
		self._VldFr = None

	@property
	def VldUntil(self):
		return self._VldUntil

	@VldUntil.setter
	def VldUntil(self, value):
		self._VldUntil = value if type(value) != base_types.auto else self.make_default("VldUntil")

	@VldUntil.deleter
	def VldUntil(self):
		del self._VldUntil
		self._VldUntil = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RstrctnTp', type=CodeOrProprietary1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldFr', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldUntil', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))