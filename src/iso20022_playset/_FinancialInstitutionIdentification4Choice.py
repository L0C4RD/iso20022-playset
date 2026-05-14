# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BICIdentifier import BICIdentifier
from ._NameAndAddress6 import NameAndAddress6

class FinancialInstitutionIdentification4Choice(base_types._BaseFieldType):

	__slots__ = ["_BIC", "_NmAndAdr"]
	@property
	def BIC(self):
		return self._BIC

	@BIC.setter
	def BIC(self, value):
		self._BIC = value if type(value) != base_types.auto else self.make_default("BIC")

	@BIC.deleter
	def BIC(self):
		del self._BIC
		self._BIC = None

	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if type(value) != base_types.auto else self.make_default("NmAndAdr")

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BIC', type=BICIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress6, min=0, max=1, mutex_group=1, array=False),
	))