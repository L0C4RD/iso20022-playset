# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text

class ProductClassification1(base_types._BaseFieldType):

	__slots__ = ["_AsstClss", "_BasePdct", "_SubCmmdty", "_SubPdct", "_TxTp"]
	@property
	def AsstClss(self):
		return self._AsstClss

	@AsstClss.setter
	def AsstClss(self, value):
		self._AsstClss = value if type(value) != base_types.auto else self.make_default("AsstClss")

	@AsstClss.deleter
	def AsstClss(self):
		del self._AsstClss
		self._AsstClss = None

	@property
	def BasePdct(self):
		return self._BasePdct

	@BasePdct.setter
	def BasePdct(self, value):
		self._BasePdct = value if type(value) != base_types.auto else self.make_default("BasePdct")

	@BasePdct.deleter
	def BasePdct(self):
		del self._BasePdct
		self._BasePdct = None

	@property
	def SubCmmdty(self):
		return self._SubCmmdty

	@SubCmmdty.setter
	def SubCmmdty(self, value):
		self._SubCmmdty = value if type(value) != base_types.auto else self.make_default("SubCmmdty")

	@SubCmmdty.deleter
	def SubCmmdty(self):
		del self._SubCmmdty
		self._SubCmmdty = None

	@property
	def SubPdct(self):
		return self._SubPdct

	@SubPdct.setter
	def SubPdct(self, value):
		self._SubPdct = value if type(value) != base_types.auto else self.make_default("SubPdct")

	@SubPdct.deleter
	def SubPdct(self):
		del self._SubPdct
		self._SubPdct = None

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if type(value) != base_types.auto else self.make_default("TxTp")

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstClss', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BasePdct', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubCmmdty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubPdct', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))