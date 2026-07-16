# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CodeOrProprietary1Choice
from . import ISODateTime

class Restriction1(base_types._BaseFieldType):

	__slots__ = ["_RstrctnTp", "_VldFr", "_VldUntil"]
	@property
	def RstrctnTp(self):
		return self._RstrctnTp

	@RstrctnTp.setter
	def RstrctnTp(self, value):
		self._RstrctnTp = value if value is not None else base_types.UninitialisedField(self, 'RstrctnTp', CodeOrProprietary1Choice, False)

	@RstrctnTp.deleter
	def RstrctnTp(self):
		del self._RstrctnTp
		self._RstrctnTp = base_types.UninitialisedField(self, 'RstrctnTp', CodeOrProprietary1Choice, False)

	@property
	def VldFr(self):
		return self._VldFr

	@VldFr.setter
	def VldFr(self, value):
		self._VldFr = value if value is not None else base_types.UninitialisedField(self, 'VldFr', ISODateTime, False)

	@VldFr.deleter
	def VldFr(self):
		del self._VldFr
		self._VldFr = base_types.UninitialisedField(self, 'VldFr', ISODateTime, False)

	@property
	def VldUntil(self):
		return self._VldUntil

	@VldUntil.setter
	def VldUntil(self, value):
		self._VldUntil = value if value is not None else base_types.UninitialisedField(self, 'VldUntil', ISODateTime, False)

	@VldUntil.deleter
	def VldUntil(self):
		del self._VldUntil
		self._VldUntil = base_types.UninitialisedField(self, 'VldUntil', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RstrctnTp', type=CodeOrProprietary1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldFr', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldUntil', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))