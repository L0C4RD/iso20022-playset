# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMDepositedMediaItem1
from . import ATMMediaType3Code
from . import ATMMediaType4Code
from . import Number

class ATMDepositedMedia4(base_types._BaseFieldType):

	__slots__ = ["_AcctSeqNb", "_MdiaCtgy", "_MdiaItm", "_MdiaTp"]
	@property
	def AcctSeqNb(self):
		return self._AcctSeqNb

	@AcctSeqNb.setter
	def AcctSeqNb(self, value):
		self._AcctSeqNb = value if value is not None else base_types.UninitialisedField(self, 'AcctSeqNb', Number, False)

	@AcctSeqNb.deleter
	def AcctSeqNb(self):
		del self._AcctSeqNb
		self._AcctSeqNb = base_types.UninitialisedField(self, 'AcctSeqNb', Number, False)

	@property
	def MdiaCtgy(self):
		return self._MdiaCtgy

	@MdiaCtgy.setter
	def MdiaCtgy(self, value):
		self._MdiaCtgy = value if value is not None else base_types.UninitialisedField(self, 'MdiaCtgy', ATMMediaType3Code, False)

	@MdiaCtgy.deleter
	def MdiaCtgy(self):
		del self._MdiaCtgy
		self._MdiaCtgy = base_types.UninitialisedField(self, 'MdiaCtgy', ATMMediaType3Code, False)

	@property
	def MdiaItm(self):
		return self._MdiaItm

	@MdiaItm.setter
	def MdiaItm(self, value):
		self._MdiaItm = value if value is not None else base_types.UninitialisedField(self, 'MdiaItm', ATMDepositedMediaItem1, True)

	@MdiaItm.deleter
	def MdiaItm(self):
		del self._MdiaItm
		self._MdiaItm = base_types.UninitialisedField(self, 'MdiaItm', ATMDepositedMediaItem1, True)

	@property
	def MdiaTp(self):
		return self._MdiaTp

	@MdiaTp.setter
	def MdiaTp(self, value):
		self._MdiaTp = value if value is not None else base_types.UninitialisedField(self, 'MdiaTp', ATMMediaType4Code, False)

	@MdiaTp.deleter
	def MdiaTp(self):
		del self._MdiaTp
		self._MdiaTp = base_types.UninitialisedField(self, 'MdiaTp', ATMMediaType4Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctSeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdiaCtgy', type=ATMMediaType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdiaItm', type=ATMDepositedMediaItem1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MdiaTp', type=ATMMediaType4Code, min=1, max=1, mutex_group=None, array=False),
	))